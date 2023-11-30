import ConversationSave

prompt = """你是一个Linux专家，用中文回答下面的问题。你的回答需要满足以下要求:
1. 你的回答必须是中文
2. 回答限制在100个字以内"""

question1 = "什么是Linux？"
question2 = "Linux的发行版有哪些？"
question3 = "Linux和Windows有什么区别？"
question4 = "我问你的第一个问题是什么？"

conv2 = ConversationSave.ConversationSave(prompt, 2)
questions = [question1, question2, question3, question4]

i = 0
for question in questions:
    i = i+1
    answer = conv2.ask(question)
    print("询问[##%d]： {%s}，回复：{%s}" % (i, question, answer))