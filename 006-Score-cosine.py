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
langchain.debug = False
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
store = FAISS.from_documents(docs, embeddings)
top_k = 4

def get_cosine(sample_embedding, base_embedding):
    return cosine_similarity(sample_embedding, base_embedding)

query = "Linux下的内核空间和用户空间怎么划分？"

query_embs = embeddings.embed_query(query)
docs_with_score = store.similarity_search_with_score(query, top_k)
for doc, score in docs_with_score:
    print("-" * 80)
    print("Score: ", score)
    text_embs = embeddings.embed_query(doc.page_content)
    cosine = get_cosine(query_embs, text_embs)
    print("cosine: ", cosine)
    print(doc.page_content)
    print("-" * 80)
