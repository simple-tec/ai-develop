from langchain.agents import Tool, initialize_agent
import myllm
import langchain
from flask import Flask, request, jsonify
from flask_cors import CORS

langchain.debug = False

llm = myllm.myllm

def Cooking(input: str) -> str:
    # print("\nCooking input:" + input + "\n")
    return "做法如下：１，加一个鸡蛋；２，切一个土豆；３，拿油炒一下，就可以出锅啦"

def search_order(input: str) -> str:
    # print("\nsearch_order input:" + input + "\n")
    return "您的的快递已到达成都市白羊区"

def faq(input: str) -> str:
    # print("\nfaq input:" + input + "\n")
    return "为了学习c语言，你可以先学习变量定义和循环控制，然后再学习c语言函数和数据结构"

def other(input: str) -> str:
    # print("\nfaq input:" + input + "\n")
    result  = llm.predict(input)
    return result

tools = [
    Tool(
        name = "Cooking",func=Cooking, 
        description="useful for when you need to answer questions about cooking"
    ),
    Tool(name="Search Order", func=search_order, 
         description="useful for when you need to answer questions about product orders"
    ),
    Tool(name="FAQ", func=faq,
         description="I am a software engineer, useful for when you need to answer questions about C language"
    ),
     Tool(name="Other", func=other,
         description="useful for when you need to answer questions about others"
    )
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def answer_question(question):
    # question = "中国的首都是哪座城市？"
    # question = "请问如何入门学习c语言？"
    result = agent.run(question)
    return result 

app = Flask(__name__)
CORS(app)
@app.route('/api/ai', methods=['POST'])
def ai():
    # 检查请求内容是否为JSON格式
    if not request.is_json:
        return jsonify({'error': 'Invalid JSON format'}), 400

    # 获取请求中的问题
    question = request.json.get('question')

    # 根据问题生成答案
    answer = answer_question(question)

    # 返回答案
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(port=8989)