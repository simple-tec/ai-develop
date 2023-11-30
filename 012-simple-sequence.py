from langchain import PromptTemplate
from langchain.chains import LLMChain,SimpleSequentialChain
import myllm

llm = myllm.myllm
en_to_zh_prompt_1 = PromptTemplate(
    template="请把下面这句话翻译成英文： \n\n {question}?", input_variables=["question"]
)

question_prompt_2 = PromptTemplate(
    template = "{english_question}", input_variables=["english_question"]
)

zh_to_cn_prompt_3 = PromptTemplate(
    input_variables=["english_answer"],
    template="请把下面这一段翻译成中文： \n\n{english_answer}?",
)

question_chain = LLMChain(llm=llm, prompt=en_to_zh_prompt_1, output_key="english_question")
qa_chain = LLMChain(llm=llm, prompt=question_prompt_2, output_key="english_answer")
answer_chain = LLMChain(llm=llm, prompt=zh_to_cn_prompt_3)

chinese_qa_chain = SimpleSequentialChain(
    chains=[question_chain, qa_chain, answer_chain], input_key="question",
    verbose=True)
answer = chinese_qa_chain.run(question="什么是linux?")
print(answer)