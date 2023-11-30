from langchain.agents import Tool, initialize_agent
import myllm
import langchain
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
question = "中国的首都是哪座城市？"
# question = "请问如何入门学习c语言？"
result = agent.run(question)
print(result)


'''
question = "我买了一件性感内衣，现在还没收到货，能麻烦帮我查一下订单吗？"
result = agent.run(question)
print(result)

question = "土豆炒鸡蛋怎么做？"
result = agent.run(question)
print(result)
'''

'''
1, agent调用llm，根据原始问题得到了正确的tool的名字，比如FAQ
2, 根据输入，调用FAQ对应的函数，得到函数的执行结果
3，agent根据第二步的执行结果，调用llm，得到最终的答案。
'''