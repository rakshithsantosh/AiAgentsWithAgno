from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

#define the llm
llm = OpenAIChat(id="gpt-5-mini")

#initialize the OpenAI chat model
agent = Agent(
    name="Basic OpenAI Agent",
    model=llm,
    markdown=True
)

agent.print_response(input="Write a short poem about AI in 4 lines.")

