from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from openai.embeddings_utils import get_embedding
import openai
import os
import constants

os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY
os.environ["OPENAI_API_BASE"] = constants.OPENAI_API_BASE_URL
openai.api_key = constants.OPENAI_API_KEY
openai.api_base = constants.OPENAI_API_BASE_URL

myllm = OpenAI()
mychat = ChatOpenAI()
myembeddings = OpenAIEmbeddings()

def my_get_embedding(text):
    return get_embedding(text, engine='text-embedding-ada-002')