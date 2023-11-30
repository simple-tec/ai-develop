from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
import os
import myllm

res = myllm.myllm.predict("你好！")
print(res)

embeddings = myllm.myembeddings
text = "This is a test query."
query_result = embeddings.embed_query(text)
# print(query_result)
print(len(query_result))
