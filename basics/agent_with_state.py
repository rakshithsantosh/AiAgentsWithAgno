from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb

#load environment variables from .env file
load_dotenv()

#define the llm
llm = OpenAIChat(id="gpt-5-mini")

# create a database
db= SqliteDb(db_file="session_state_db/shopping.db")

# define a tool that adds items to shopping list

def add_item(session_state:dict, item:str) -> str:
    """add an item to the shopping list"""
    shopping_list = session_state["shopping_list"]
    shopping_list.append(item)
    session_state["shopping_list"] = shopping_list
    return f"Added {item} to your shopping list."

session_id = "session_state_1"

#initialize the OpenAI chat model
agent = Agent(
    name="Basic OpenAI Agent with state",
    model=llm,
    markdown=True,
    session_state={"shopping_list":[]},
    db=db,
    instructions="You are a helpful shopping assistant. Help the user create and manage their shopping list.You have access to shopping list {shopping_list}",
    stream=True,
    tools=[add_item],
    session_id=session_id,
    user_id="user_1",
    add_history_to_context=True,
    add_session_state_to_context=True,
    num_history_runs=5,
)

agent.print_response("I want to buy apples and bananas. Add them to my shopping list.")

print(f"Current shopping list: {agent.session_state['shopping_list']}")