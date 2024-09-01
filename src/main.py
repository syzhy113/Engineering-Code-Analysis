import warnings
warnings.filterwarnings("ignore")
import asyncio
import os
from Tools import *
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_core.tools import render_text_description
from Agent.Action import Action
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from Agent.ReAct import ReActAgent
from langchain_openai import ChatOpenAI
import json


with open('config.json') as f:
    config = json.load(f)
    os.environ["GIT_KEY"] = config["GIT_KEY"]
    os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
    os.environ["OPENAI_BASE_URL"] = config["OPENAI_BASE_URL"]

from typing import Annotated
from os.path import exists
from langgraph.graph.message import add_messages

from typing import Literal

from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, StateGraph
from typing import TypedDict, Optional
from Models.Github import *


class State(TypedDict):
    messages: Annotated[list, add_messages]
    dict_struct: Optional[str] = None
    python_code_list: Optional[list]


tools = [python_tool, finish_placeholder, core.as_tool()]

model_name = "gpt-4o"

model = ChatOpenAI(model=model_name)

agent = ReActAgent(
    llm=model,
    tools=tools,
    main_prompt_file="./prompts/main/sample_agent.txt",
    max_thought_steps=5,
)

large_agent = ReActAgent(
    llm=model,
    tools=tools,
    main_prompt_file="./prompts/main/main.txt",
    max_thought_steps=20,
)


def should_agent(state: State) -> Literal["agent", "sample_agent", "__end__"]:
    messages = state["messages"]
    last_message = messages[-1].content
    if last_message == "NO":
        return "sample_agent"
    elif last_message == "YES":
        return "agent"
    else:
        print("无结果")
        return END


def no_dict(state: State) -> Literal["sample_agent", "agent_select"]:
    dict_str = state["dict_struct"]
    if dict_str:
        return "agent_select"
    return "sample_agent"


def extract_json_action(text: str) -> str | None:
    json_pattern = re.compile(r'```json(.*?)```', re.DOTALL)
    matches = json_pattern.findall(text)
    if matches:
        last_json_str = matches[-1]
        return last_json_str
    return None


async def dict_list(state: State, config: RunnableConfig):
    contents = "不存在 Start-*&^%"
    output_parser = PydanticOutputParser(pydantic_object=Action)
    with open('./prompts/main/dict_list_prompt.txt', 'r', encoding='utf-8') as f:
        prompt = ChatPromptTemplate.from_messages([HumanMessagePromptTemplate.from_template(f.read())]).partial(
            tools=render_text_description([return_dict_tool]),
            tool_names=','.join([return_dict_tool.name]),
            format_instructions=output_parser.get_format_instructions(),
        )
    messages = state["messages"]
    run_model = (prompt | model | StrOutputParser())
    short_term_memory = []
    robust_parser = OutputFixingParser.from_llm(
        parser=output_parser,
        llm=model
    )
    time = 5
    while contents.find('不存在') != -1 and time > 0:
        time -= 1
        if contents.find('Start-*&^%') != -1:
            input_temp = {'input': messages[0].content, "agent_scratchpad": short_term_memory}
        else:
            input_temp = {'input': messages[0].content + contents, "agent_scratchpad": short_term_memory}
        response = await run_model.ainvoke(input_temp, config)
        json_action = extract_json_action(response)
        action = robust_parser.parse(json_action)
        response = return_dict_tool.run(action.args)
        if response == "NO":
            break
        if response.find('github') != -1:
            repo_full_name = parse_github_url(response)  # 提取仓库信息
            try:
                branch_name = "master"
                repo = g.get_repo(repo_full_name)
                contents = repo.get_contents("", ref=branch_name)
                contents = directory_contents2str_github(contents=contents, repo=repo, branch_name=branch_name)
                core.set_repo_branch(repo, branch_name)
            except:
                pass

            try:
                branch_name = "main"
                repo = g.get_repo(repo_full_name)
                contents = repo.get_contents("", ref=branch_name)
                contents = directory_contents2str_github(contents=contents, repo=repo, branch_name=branch_name)
                core.set_repo_branch(repo, branch_name)
            except:
                pass
        else:
            if exists(response):
                contents = directory_contents2str(response)
            else:
                contents = '不存在该路径，请重新确认'

    return {"messages": response, 'dict_struct': contents}


async def call_agent(state: State, config: RunnableConfig):
    messages = state["messages"][-3]
    large_agent.work_dir = state["dict_struct"]
    response = large_agent.run(messages.content, chat_history, verbose=True)
    return {"messages": response}


async def select_model(state: State, config: RunnableConfig):
    with open('./prompts/main/choose_agent.txt', 'r', encoding='utf-8') as f:
        prompt = ChatPromptTemplate.from_messages([HumanMessagePromptTemplate.from_template(f.read())])
    messages = state["messages"]
    run_model = (prompt | model | StrOutputParser())
    input_temp = {'input': messages[0].content}
    response = await run_model.ainvoke(input_temp, config)
    return {"messages": response}


async def call_model(state: State, config: RunnableConfig):
    messages = state["messages"][-3]
    agent.work_dir = state["dict_struct"]
    response = agent.run(messages.content, chat_history, verbose=True)

    return {"messages": response}


async def all_in_all_model(state: State, config: RunnableConfig):
    messages = state["messages"][-1]
    input_temp = {
        "input": messages,
    }
    with open('./prompts/main/allinall_prompt.txt', 'r', encoding='utf-8') as f:
        prompt = ChatPromptTemplate.from_messages([HumanMessagePromptTemplate.from_template(f.read())])
    run = prompt | model | StrOutputParser()
    response = ""
    async for s in run.astream(input=input_temp):
        response += s
    print(f"{response}\n")
    return {"messages": response}


chat_history = ChatMessageHistory()
workflow = StateGraph(State)

workflow.add_node("dict_list", dict_list)
workflow.add_node("agent_select", select_model)
workflow.add_node("sample_agent", call_model)
workflow.add_node("agent", call_agent)
workflow.add_node("all_agent", all_in_all_model)

workflow.add_edge(START, "dict_list")
workflow.add_edge("dict_list", "agent_select")
workflow.add_edge("sample_agent", "all_agent")
workflow.add_edge("agent", "all_agent")
workflow.add_edge("all_agent", END)

workflow.add_conditional_edges(
    "dict_list",
    no_dict,
)

workflow.add_conditional_edges(
    "agent_select",
    should_agent,
)

app = workflow.compile()


async def generate(inputs):
    async for event in app.astream_events({"messages": inputs}, version="v1"):
        kind = event["event"]
        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content


async def main():
    human_icon = "\U0001F468"
    ai_icon = "\U0001F916"

    while True:
        task = input(f"{ai_icon}：有什么可以帮您？\n{human_icon}：")
        if task.strip().lower() == "quit":
            break
        await generate(task)

if __name__ == "__main__":
    asyncio.run(main())
