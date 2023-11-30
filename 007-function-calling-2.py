import openai
import constants
import os
import json

openai.api_key = constants.OPENAI_API_KEY
openai.api_base = constants.OPENAI_API_BASE_URL

# define a function calling
def get_toy_info(toy_name: str):
    toy_info = {
        "name": toy_name,
        "price": "10.99",
    }
    return json.dumps(toy_info)

# define get_toy_info's description
functions = [
    {
        "name": "get_toy_info",
        "description": "Get name and price of a toy of the restaurant",
        "parameters": {
            "type": "object",
            "properties": {
                "toy_name": {
                    "type": "string",
                    "description": "The name of the toy, e.g. Salami",
                },
            },
            "required": ["toy_name"],
        },
    }
]

# get function_call info by query firstly
def chat(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
        functions=functions,
    )
    message = response["choices"][0]["message"]
    return message

query = "How much does toy Lego cost?"
message = chat(query)
print(f"message = {message}")

# run openai function calling secondly
if message.get("function_call"):
    # 解析第一次调用的时候返回的 toy 信息
    function_name = message["function_call"]["name"]
    toy_name = json.loads(message["function_call"] ["arguments"]).get("toy_name")
    print(f"toy_name = {toy_name}")
    # 这里将 chat 小助手函数的响应结果提取后，传递 function_response
    function_response = get_toy_info(
        toy_name=toy_name 
    )

    second_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query},
            message,
            {
                "role": "function",
                "name": function_name,
                "content": function_response, # function calling 的 content 是 get_toy_info 函数 
            },
        ],
    )
print(f"second_response_all = {second_response}")
print(second_response["choices"][0]["message"])
