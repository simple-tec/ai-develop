#!pip install sentence_transformers
#!pip install langchain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import HuggingFaceInstructEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="GanymedeNil/text2vec-large-chinese", model_kwargs={'device': "cpu"})
sentence = '你叫什么名字'
vec = embeddings.embed_documents(sentence)
print(vec)
print(len(vec))
