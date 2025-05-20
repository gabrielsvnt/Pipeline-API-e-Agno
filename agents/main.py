from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.postgres import PostgresTools
from dotenv import load_dotenv
import os   
load_dotenv()

# Initialize PostgresTools with connection details
postgres_tools = PostgresTools(
    host = os.getenv("POSTGRES_HOST"),
    port = os.getenv("POSTGRES_PORT"),
    db_name = os.getenv("POSTGRES_DB_NAME"),
    user = os.getenv("POSTGRES_USER"),
    password = os.getenv("POSTGRES_PASSWORD"),
    table_schema = os.getenv("POSTGRES_TABLE_SCHEMA"),
)

# Create an agent with the PostgresTools
agent = Agent(
     model=Groq(id="llama-3.3-70b-versatile"),
    tools=[postgres_tools])

agent.print_response("Fale com todas as tabelas do banco de dados", markdown=True)

agent.print_response("""
Analise a tabela bitcoin_dados e forneça um resumo dos dados contidos nela. Ocultando as colunas que não são relevantes para o resumo.
""")