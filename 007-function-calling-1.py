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
        "description": "Get name and price of a toy",
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

'''
result = chat("What is the capital of china?")
print(f"result = {result}")
'''

query = "How much does toy Lego cost?"
message = chat(query)
print(f"message = {message}")