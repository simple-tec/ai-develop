import openai, os
import constants
import requests

openai.api_key = constants.OPENAI_API_KEY
openai.api_base = constants.OPENAI_API_BASE_URL
prompt = "一个屌丝程序员想实现财富自由，朋克风格"
# prompt = "一个屌丝程序员努力学习linux操作系统,朋克风格"


# call the OpenAI API
generation_response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024", 
    response_format="url",
)

# print response
print(generation_response)