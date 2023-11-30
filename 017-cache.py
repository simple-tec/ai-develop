import myllm
from langchain.schema import HumanMessage,SystemMessage
import langchain
from langchain.cache import InMemoryCache
langchain.debug = False

langchain.llm_cache = InMemoryCache()
llm = myllm.myllm
mychat = myllm.mychat
text = "给我讲一个笑话"
result = llm.predict(text)
print(result)

text = "给我讲一个笑话"
result = llm.predict(text)
print(result)