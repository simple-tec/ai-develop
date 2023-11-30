import os, requests, json, sys
import constants

API_TOKEN = constants.HF_TOKEN

model = "intfloat/multilingual-e5-large"
API_URL = f"https://api-inference.huggingface.co/models/{model}"
headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}

def query(payload, api_url=API_URL, headers=headers):
    data = json.dumps(payload)
    response = requests.request("POST", api_url, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

question = "今天天气真不错！"
data = query({"inputs" : question, "wait_for_model" : True}, api_url=API_URL)

print(data)
print(len(data))