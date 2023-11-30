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
first = True
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

# save to vector store
embeddings = myllm.myembeddings
CONNECTION_STRING = PGVector.connection_string_from_db_params(
     driver=os.environ.get("PGVECTOR_DRIVER", "psycopg2"),
     host=os.environ.get("PGVECTOR_HOST", "121.89.247.179"),
     port=int(os.environ.get("PGVECTOR_PORT", "5432")),
     database=os.environ.get("PGVECTOR_DATABASE", "postgres"),
     user=os.environ.get("PGVECTOR_USER", "postgres"),
     password=os.environ.get("PGVECTOR_PASSWORD", "admin"),
)
COLLECTION_NAME = "table_schema"
if first:
    print("prepare store")
    store = PGVector(
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
        embedding_function=embeddings,
        pre_delete_collection=True,
    )
    for doc in docs:
        store.add_documents([doc])
else: 
    print("using exist store")
    store = PGVector(
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
        embedding_function=embeddings,
    )
top_k = 1


# initial QA Retriever
retriever=store.as_retriever(search_kwargs={"k": top_k})
llm = myllm.myllm
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=False, verbose=False)

# ask and answer 
query = "Linux下的内核空间和用户空间怎么划分？"
result = qa_chain.run(query)
print(result)
