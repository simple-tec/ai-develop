from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain
import myllm
llm = myllm.myllm
conversation_with_summary = ConversationChain(
    llm=llm,
    memory=ConversationSummaryMemory(llm=llm),
    verbose=True
)
conversation_with_summary.run(input="什么是Linux?") 
conversation_with_summary.run(input="什么是Windows？") 
conversation_with_summary.run(input="什么是QNX？") 
conversation_with_summary.run(input="什么是VxWorks？")