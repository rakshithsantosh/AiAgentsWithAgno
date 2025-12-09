from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.team import Team

from dotenv import load_dotenv

#load the api keys from .env file
load_dotenv()

#create 2 agents
## 1 news search agent
## 2 web search agent

#define the model
llm = OpenAIChat(id="gpt-5-mini")

#news search agent
news_agent = Agent(
    id="news_agent",
    name="News Search Agent",
    model=llm,
    role="You are a helpful assistant that specializes in searching for the latest news articles on various topics.",
    instructions="When given a topic, search for the latest news articles and provide a summary of the findings.",
    tools=[DuckDuckGoTools()],
)

#web search agent
web_agent = Agent(
    id="web_agent",
    name="Web Search Agent",
    model=llm,
    role="You are a helpful assistant that specializes in searching for information on the web.",
    instructions="When given a topic, search for information on the web and provide a summary of the findings.",
    tools=[DuckDuckGoTools()],
)

# form the team
travel_agent = Team(
    members=[news_agent, web_agent],
    name="Travel Assistant Team",
    instructions="You are a team of agents that help users plan their travels by searching for the latest news and web information about travel destinations.",
    id="Travel_agent",
    role="Team of agents to help users plan their travels",
    stream=True,
    markdown=True,
    model=llm,
)

travel_agent.cli_app(stream=True, markdown=True)