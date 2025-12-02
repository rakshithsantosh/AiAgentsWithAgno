from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.in_memory import InMemoryDb
from dotenv import load_dotenv

#load environment variables from a .env file
load_dotenv()

#initialize the language model
llm = OpenAIChat(id="gpt-3.5-turbo")

# add session id
session_id="session_id" 

# create a database
db = InMemoryDb()

# in memory db uses system ram to store data temporarily

#initialize the agent with memory
agent = Agent(
    model=llm,
    name="Agent with Memory",
    db=db,
    stream=True,
    markdown=True,
    session_id=session_id,
    add_history_to_context=True,
    num_history_runs=3,
)

#give inputs to the agent
agent.print_response(input="hi my name is Rakshith")

agent.print_response(input="what is my name?")