import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI, OpenAIEmbeddings, AzureChatOpenAI, AzureOpenAIEmbeddings


class ChatModelFactory:
    model_params = {
        "temperature": 0,
        "model_kwargs": {"seed": 42},
    }

    @classmethod
    def get_model(cls, model_name: str, use_azure: bool = False):
        if "gpt" in model_name:
            if not use_azure:
                return ChatOpenAI(model=model_name, **cls.model_params)
            else:
                return AzureChatOpenAI(
                    azure_deployment=model_name,
                    api_version="2024-05-01-preview",
                    **cls.model_params
                )
        elif model_name == "qwen2":
            # 换成开源模型试试
            # https://siliconflow.cn/
            # 一个 Model-as-a-Service 平台
            # 可以通过与 OpenAI API 兼容的方式调用各种开源语言模型。
            return ChatOpenAI(
                model="alibaba/Qwen2-72B-Instruct",  # 模型名称
                openai_api_key=os.getenv("SILICONFLOW_API_KEY"),  # 在平台注册账号后获取
                openai_api_base="https://api.siliconflow.cn/v1",  # 平台 API 地址
                **cls.model_params,
            )

    @classmethod
    def get_default_model(cls):
        return cls.get_model("gpt-3.5-turbo")


class EmbeddingModelFactory:

    @classmethod
    def get_model(cls, model_name: str, use_azure: bool = False):
        if model_name.startswith("text-embedding"):
            if not use_azure:
                return OpenAIEmbeddings(model=model_name)
            else:
                return AzureOpenAIEmbeddings(
                    azure_deployment=model_name,
                    openai_api_version="2024-05-01-preview",
                )
        else:
            raise NotImplementedError(f"Model {model_name} not implemented.")

    @classmethod
    def get_default_model(cls):
        return cls.get_model("text-embedding-ada-002")
