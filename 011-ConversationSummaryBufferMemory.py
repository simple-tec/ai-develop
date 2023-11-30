from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
import myllm
import langchain
llm = myllm.myllm
conversation_with_summary = ConversationChain(
    llm=llm,
    # We set a very low max_token_limit for the purposes of testing.
    memory=ConversationSummaryBufferMemory(llm=llm, max_token_limit=10),
    verbose=True,
)
conversation_with_summary.run(input="什么是Linux?") 
conversation_with_summary.run(input="什么是Windows？") 
conversation_with_summary.run(input="什么是QNX？") 
conversation_with_summary.run(input="什么是VxWorks？")