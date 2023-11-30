from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
import myllm

conversation_with_summary = ConversationChain(
    llm=myllm.myllm,
    # We set a low k=2, to only keep the last 2 interactions in memory
    memory=ConversationBufferWindowMemory(k=2),
    verbose=True
)
conversation_with_summary.run(input="什么是Linux？") 
conversation_with_summary.run(input="什么是Windows？") 
conversation_with_summary.run(input="什么是QNX？") 
conversation_with_summary.run(input="什么是VxWorks？")