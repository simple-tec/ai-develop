from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
import myllm

chatllm = myllm.myllm

class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""


    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ")

template = """你是一个有帮助的助手，用于生成逗号分隔的列表。
用户将传入一个类别，然后你应该生成该类别中的5个对象，并以逗号分隔的列表形式返回。
仅返回一个逗号分隔的列表，不要返回其他内容。"""
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
chain = LLMChain(
    llm=chatllm,
    prompt=chat_prompt,
    output_parser=CommaSeparatedListOutputParser()
)
res = chain.run("水果")
print(res)