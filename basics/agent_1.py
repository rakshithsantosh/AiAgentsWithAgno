from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb

#load environment variables from .env file
load_dotenv()

#define the llm
llm = OpenAIChat(id="gpt-5-mini")

# create a database
db= SqliteDb(db_file="session_state_db/basic_demo.db")

#create session state dictionary
user_info={
    "user_name": "Alice",
    "favorite_color": "blue",
    "hobby": "painting"
}

#initialize the OpenAI chat model
agent = Agent(
    name="Basic OpenAI Agent with state",
    model=llm,
    markdown=True,
    session_state=user_info,
    db=db,
    stream=True,
    session_id="session_state_1",
    user_id="user_1",
    add_history_to_context=True,
    add_session_state_to_context=True,
    num_history_runs=5,
)

agent.print_response(input="Write a short poem about me in 4 lines.")

# if we pass a session state with in agent.print_response method, it will update the existing session state

