import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "server", "inventory.db"))

load_dotenv()

db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH}")
llm = ChatOpenAI(model="gpt-4o-mini")

sql_prompt = PromptTemplate.from_template(
    """
You are an expert SQLite query generator.

The database has multiple related tables. 
If answering the question requires data from more than one table,
you MUST use the appropriate JOINs.

Common relationships:
- sales.product_id = products.id
- inventory.product_id = products.id
- orders.customer_id = customers.id

Rules:
- Return ONLY valid SQL.
- Never include explanations or text.
- If the question refers to product information, ALWAYS join sales → products to get the product name.

Question: {question}
"""
)

answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

 Question: {question}
 SQL Query: {query}
 SQL Result: {result}
 Answer: """
)

generate_query = sql_prompt | llm | StrOutputParser()
rephrase_answer = answer_prompt | llm | StrOutputParser()


def execute_query(query):
    return db.run(query)


def clean_sql(sql):
    return sql.replace("```sql", "").replace("```", "").strip()


chain = (
    RunnablePassthrough.assign(query=generate_query).assign(
        result=(
            RunnableLambda(lambda x: clean_sql(x["query"]))
            | RunnableLambda(execute_query)
        )
    )
    | rephrase_answer
)

result = chain.invoke(
    {"question": "What is the minimum order quantity for a External SSD 1TB"}
)

print(result)
