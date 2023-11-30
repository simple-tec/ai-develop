import myllm
from langchain.schema import HumanMessage,SystemMessage
import langchain
import langchain
langchain.debug = False

llm = myllm.myllm
mychat = myllm.mychat
text = "给我讲一个笑话"
result = llm.predict(text)
print(result)

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to Chinese."),
    HumanMessage(content="I love programming.")
]
result = mychat.predict_messages(messages)
print(result)
