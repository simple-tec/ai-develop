import openai
import os
import constants
import getpass
from pathlib import Path
import time
from langchain.vectorstores import FAISS

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import TokenTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector
from langchain.document_loaders import TextLoader
from langchain.document_loaders import JSONLoader

from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from openai.embeddings_utils import cosine_similarity
import myllm
import langchain
langchain.debug = True
# load file
loader = TextLoader("./data/linux-kernel-qa.txt")
documents = loader.load()
print(f'documents:{len(documents)}')

# initial TextSplitter
text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=64, 
        chunk_overlap=0,
        separators=["\n\n"])

# split file
docs = text_splitter.split_documents(documents)
print(f'splited documents:{len(docs)}')
for index, doc in enumerate(docs):
    print(f"{index}: {doc}")

embeddings = myllm.myembeddings
db = FAISS.from_documents(docs, embeddings)


top_k = 1

# initial QA Retriever
retriever=db.as_retriever(search_kwargs={"k": top_k})
llm = myllm.myllm
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=False, verbose=False)

# ask and answer 
query = "Linux下的内核空间和用户空间怎么划分？"
result = qa_chain.run(query)
print(result)

'''
top_k = 1
query = "Linux下的内核空间和用户空间怎么划分？"
retriever=db.as_retriever(search_kwargs={"k": top_k})

docs = retriever.get_relevant_documents(query)
for index, doc in enumerate(docs):
    print(f"{index}: {doc}")

query = "Linux下的内核空间和用户空间怎么划分？"
retriever = db.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": .8})
docs = retriever.get_relevant_documents(query)
print("++++++++++++++++++++++++++++++++++++++++++")
for index, doc in enumerate(docs):
    print(f"{index}: {doc}")

'''