from langchain import PromptTemplate, OpenAI, LLMChain
import myllm

prompt_template = "What is a good name for a company that makes {product}?"

llm = myllm.myllm
llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)
input_list = [
    {"product": "socks"},
    {"product": "computer"},
    {"product": "shoes"}
]
res = llm_chain.run("colorful socks")
print(res)
res = llm_chain.generate(input_list)
print(res)