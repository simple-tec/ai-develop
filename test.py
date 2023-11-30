import myllm
from langchain.schema import HumanMessage,SystemMessage
import langchain
import langchain
from langchain import PromptTemplate
from langchain.chains import LLMChain
langchain.debug = False
import myllm
llm = myllm.myllm

prompt = '''
You are an agent designed to interact with a SQL database.\nGiven an input question, create a syntactically correct sqlite query to run, then look at the results of the query and return the answer.\nUnless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 10 results.\nYou can order the results by a relevant column to return the most interesting examples in the database.\nNever query for all the columns from a specific table, only ask for the relevant columns given the question.\nYou have access to tools for interacting with the database.\nOnly use the below tools. Only use the information returned by the below tools to construct your final answer.\nYou MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.\n\nDO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.\n\nIf the question does not seem related to the database, just return \"I don't know\" as the answer.\n\n\nsql_db_query: Input to this tool is a detailed and correct SQL query, output is a result from the database. If the query is not correct, an error message will be returned. If an error is returned, rewrite the query, check the query, and try again. If you encounter an issue with Unknown column 'xxxx' in 'field list', using sql_db_schema to query the correct table fields.\nsql_db_schema: Input to this tool is a comma-separated list of tables, output is the schema and sample rows for those tables. Be sure that the tables actually exist by calling sql_db_list_tables first! Example Input: 'table1, table2, table3'\nsql_db_list_tables: 
Input is an empty string, output is a comma separated list of tables in the database.\nsql_db_query_checker: Use this tool to double check if your query is correct before executing it. Always use this tool before executing a query with sql_db_query!\n\nUse the following format:\n\nQuestion: the input question you 
must answer\nThought: you should always think about what to do\nAction: the action to take, should be one of [sql_db_query, sql_db_schema, sql_db_list_tables, sql_db_query_checker]\nAction Input: the input to the action\nObservation: the result of the action\n... (this Thought/Action/Action Input/Observation can repeat N times)\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question\n\nBegin!\n\nQuestion: Describe the playlisttrack table\nThought: I should look at the tables 
in the database to see what I can query.  Then I should query the schema of the most relevant tables.
'''
print(prompt)