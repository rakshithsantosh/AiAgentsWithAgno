from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Step, Workflow,Parallel
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.hackernews import HackerNewsTools

from dotenv import load_dotenv

load_dotenv()

#create the model
model = OpenAIChat(id="gpt-4.1-mini")

# define agents

google_agent = Agent(
    id="google-search-agent",
    name="Google Search Agent",
    instructions="You are an expert web search agent using google search. provide accurate and relevant information based on user input. Use the provided tools to gather accurate and relevant information on the given topic.",
    model=model,
    tools=[GoogleSearchTools()]
)

duckduckgo_agent = Agent(
    id="duckduckgo-search-agent",
    name="DuckDuckGo Search Agent", 
    instructions="You are an expert web search agent using duckduckgo search. provide accurate and relevant information based on user input. Use the provided tools to gather accurate and relevant information on the given topic.",
    model=model,
    tools=[DuckDuckGoTools()]
)

hackernews_agent = Agent(
    id="hackernews-search-agent",
    name="HackerNews Search Agent",
    instructions="You are an expert web search agent using hackernews search. provide accurate and relevant information based on user input. Use the provided tools to gather accurate and relevant information on the given topic.",
    model=model,
    tools=[HackerNewsTools()]
)

# report generation agent 

report_generation = Agent(
    id="report-generation-agent",
    name="Report Generation Agent",
    model=model,
    instructions="You are an expert report generator. Compile the information provided by the web search agents into a comprehensive and coherent report. Ensure that the report is well-structured and covers all relevant aspects of the topic.",
)

# design the steps
google_search_step = Step(
    name="Google Search Step",
    agent=google_agent,
    description="Gathers information using Google Search."
)

duckduckgo_search_step = Step(
    name="DuckDuckGo Search Step",
    agent=duckduckgo_agent,
    description="Gathers information using DuckDuckGo Search."
)

hackernews_search_step = Step(
    name="HackerNews Search Step",
    agent=hackernews_agent,
    description="Gathers information using HackerNews Search."
)

# report generation step
report_generation_step = Step(
    name="Report Generation Step",
    agent=report_generation,
    description="Compiles information from web search agents into a comprehensive report."
)

#parallel step

parallel_steps = Parallel(
    google_search_step,
    duckduckgo_search_step,
    hackernews_search_step,
    name="Web Search Parallel Step",
    description="Executes multiple web search agents in parallel to gather information from different sources."
)

# workflow definition

parallel_workflow = Workflow(
    id="web-search-parallel-workflow",
    name="Web Search Parallel Workflow",
    steps=[parallel_steps, report_generation_step],
    description="A workflow that gathers information from multiple web search agents in parallel and then compiles the information into a comprehensive report."
)

# execute the workflow
parallel_workflow.print_response(input="analyse the acceptance of agno over langchain", stream=True, markdown=True)