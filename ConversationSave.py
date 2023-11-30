import openai
import constants
openai.api_key = constants.OPENAI_API_KEY
openai.api_base = constants.OPENAI_API_BASE_URL
import langchain
langchain.debug = True

class ConversationSave:
    def __init__(self, prompt, index_of_round):
        self.prompt = prompt
        self.index_of_round = index_of_round
        self.messages = []
        self.messages.append({"role": "system", "content": self.prompt})

    def ask(self, question):
        try:
            self.messages.append({"role": "user", "content": question})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                temperature=0.5,
                max_tokens=2048,
                top_p=1,
            )
        except Exception as e:
            print(e)
            return e

        message = response["choices"][0]["message"]["content"]
        # num_of_tokens = response['usage']['total_tokens']
        self.messages.append({"role": "assistant", "content": message})
        
        if len(self.messages) > self.index_of_round*2 + 1:
             # self.messages[0]保存了system role info
             # self.messages[1]保存了第一个问题的问题
             # self.messages[2]保存了第一个问题的答案
             # 所以self.messages[1:3]就表示第一个问题的问题和答案
            print(f"delete first question & answer: {self.messages[1:3]}")
            del self.messages[1:3]
        return message