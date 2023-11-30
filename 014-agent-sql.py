from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
import myllm
import langchain
langchain.debug = True
llm = myllm.myllm

db = SQLDatabase.from_uri("sqlite:///./data/Chinook.db")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

result = agent_executor.run("Describe the playlisttrack table")
print(result)

'''
1，调用llm，得到了需要使用的tool，也就是sql_db_list_tables
2，调用sql_db_list_tables，得到数据库里的所有的table的名字
3，调用llm，得到下接下来要使用的tool，也就是sql_db_schema
4，调用sql_db_schema，得到对应的表的create sql语句和前3行的数据
5，调用llm，得到了最终的答案
'''

'''
result = agent_executor.run(
    "List the total sales per country. Which country's customers spent the most?"
)
print(result)
'''