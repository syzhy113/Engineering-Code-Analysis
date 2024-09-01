import re
from typing import List, Tuple

from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from langchain_core.language_models.chat_models import BaseChatModel
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from langchain.schema.output_parser import StrOutputParser
from langchain.tools.base import BaseTool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import render_text_description
from pydantic import ValidationError
from langchain_core.prompts import HumanMessagePromptTemplate
from Tools.githubTool import github_core

from Agent.Action import Action
from Utils.CallbackHandlers import *


class ReActAgent:
    """AutoGPT：基于Langchain实现"""

    @staticmethod
    def __format_thought_observation(thought: str, action: Action, observation: str) -> str:
        ret = re.sub(r'```json(.*?)```', '', thought, flags=re.DOTALL)
        ret += "\n" + str(action) + "\n返回结果:\n" + observation
        return ret

    @staticmethod
    def __extract_json_action(text: str) -> str | None:
        json_pattern = re.compile(r'```json(.*?)```', re.DOTALL)
        matches = json_pattern.findall(text)
        if matches:
            last_json_str = matches[-1]
            return last_json_str
        return None

    def __init__(
            self,
            llm: BaseChatModel,
            tools: List[BaseTool],
            main_prompt_file: str,
            max_thought_steps: Optional[int] = 10,
            work_dir: str = None,
    ):
        self.llm = llm
        self.tools = tools
        self.work_dir = work_dir
        self.max_thought_steps = max_thought_steps
        self.github_core = github_core()

        self.output_parser = PydanticOutputParser(pydantic_object=Action)
        self.robust_parser = OutputFixingParser.from_llm(
            parser=self.output_parser,
            llm=llm
        )

        self.main_prompt_file = main_prompt_file

        self.__init_prompt_templates()
        self.__init_chains()

        self.verbose_handler = ColoredPrintHandler(color=THOUGHT_COLOR)

    def __init_prompt_templates(self):
        with open(self.main_prompt_file, 'r', encoding='utf-8') as f:
            self.prompt = ChatPromptTemplate.from_messages(
                [
                    MessagesPlaceholder(variable_name="chat_history"),
                    HumanMessagePromptTemplate.from_template(f.read()),
                ]
            ).partial(
                tools=render_text_description(self.tools),
                tool_names=','.join([tool.name for tool in self.tools]),
                format_instructions=self.output_parser.get_format_instructions(),
            )

    def __init_chains(self):
        # 主流程的chain
        self.main_chain = (self.prompt | self.llm | StrOutputParser())

    def __find_tool(self, tool_name: str) -> Optional[BaseTool]:
        for tool in self.tools:
            if tool.name == tool_name:
                return tool
        return None

    def __step(self,
               task,
               short_term_memory,
               chat_history,
               verbose=False
               ) -> Tuple[Action, str]:

        """执行一步思考"""

        inputs = {
            "input": task,
            "agent_scratchpad": "\n".join(short_term_memory),
            "chat_history": chat_history.messages,
            "work_dir": self.work_dir,
        }

        config = {
            "callbacks": [self.verbose_handler]
            if verbose else []
        }
        response = ""
        for s in self.main_chain.stream(inputs, config=config):
            response += s

        json_action = self.__extract_json_action(response)

        action = self.robust_parser.parse(
            json_action if json_action else response
        )
        return action, response

    def __exec_action(self, action: Action) -> str:
        # 查找工具
        tool = self.__find_tool(action.name)
        if tool is None:
            observation = (
                f"Error: 找不到工具或指令 '{action.name}'. "
                f"请从提供的工具/指令列表中选择，请确保按对顶格式输出。"
            )
        else:
            try:
                # 执行工具
                observation = tool.run(action.args)
            except ValidationError as e:
                # 工具的入参异常
                observation = (
                    f"Validation Error in args: {str(e)}, args: {action.args}"
                )
            except Exception as e:
                # 工具执行异常
                observation = f"Error: {str(e)}, {type(e).__name__}, args: {action.args}"

        return observation

    def extract_between_markers(self, s, marker1, marker2):
        """
        Extracts a substring from 's' that is between two markers 'marker1' and 'marker2'.

        Parameters:
        - s (str): The string from which to extract the substring.
        - marker1 (str): The start marker.
        - marker2 (str): The end marker.

        Returns:
        - str: The extracted substring. If the markers are not found, an empty string is returned.
        """
        start_pos = s.find(marker1)
        end_pos = s.find(marker2)

        if start_pos != -1 and end_pos != -1:
            return s[start_pos + len(marker1):end_pos]
        else:
            return "标志不存在"

    def run(
            self,
            task: str,
            chat_history: ChatMessageHistory,
            verbose=False
    ) -> str:
        """
        运行智能体
        :param task: 用户任务
        :param chat_history: 对话上下文（长时记忆）
        :param verbose: 是否显示详细信息
        """
        short_term_memory = []

        thought_step_count = 0

        reply = ""

        while thought_step_count < self.max_thought_steps:
            if verbose:
                self.verbose_handler.on_thought_start(thought_step_count)

            action, response = self.__step(
                task=task,
                short_term_memory=short_term_memory,
                chat_history=chat_history,
                verbose=verbose,
            )

            if action.name == "FINISH":
                reply = response
                break

            observation = self.__exec_action(action)

            if verbose:
                self.verbose_handler.on_tool_end(observation)

            short_term_memory.append(
                self.__format_thought_observation(
                    response, action, observation
                )
            )

            thought_step_count += 1

        if thought_step_count >= self.max_thought_steps:
            reply = "抱歉，我没能完成您的任务。"

        chat_history.add_user_message(task)
        chat_history.add_ai_message(reply)
        return reply
