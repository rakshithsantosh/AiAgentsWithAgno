from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow import Step, Workflow

from dotenv import load_dotenv

load_dotenv()

#create the model
model = OpenAIChat(id="gpt-4.1-mini")

#create essay writing agent
essay_agent = Agent(
    id="essay-writer",
    name="Essay Writer Agent",
    instructions="You are an expert essay writer. Write well-structured and coherent essays on given topics.Limit your response to a maximum of 500 words.",
    model=model
)

#extraction agent
extraction_agent = Agent(
    id="extraction-agent",
    name="Information Extraction Agent",
    instructions="You are an expert information extractor. Extract key points and relevant information from the provided text.Summarize the key points in a consiese manner.",
    model=model
)

# define the steps of the workflow

essay_writing_step = Step(
    name="Essay Writing Step",
    agent=essay_agent,
    description="Generates an essay on a given topic."
)

extraction_step = Step(
    name="Information Extraction Step",
    agent=extraction_agent,
    description="Extracts key points and relevant information from the provided text."
)

# workflow definition

workflow = Workflow(
    id="essay-workflow",
    name="Essay Writing and Information Extraction Workflow",
    steps=[essay_writing_step, extraction_step],
    description="A workflow that generates an essay on a given topic and then extracts key points from the essay."
)

# execute the workflow

workflow.print_response(input="the topic is growth prospects of aether industries", stream=True, markdown=True)



