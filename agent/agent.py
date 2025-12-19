from google.adk.agents.llm_agent import LlmAgent
from .sub_agents import sub_agents 

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant that answers user questions across different domains, providing clear and understandable information.",
    instruction=(
        "Answer user questions in plain, readable language, summarizing key points clearly. "
        "Avoid returning raw data or technical formats; instead, translate the information into concise, natural language. "
        "Adjust the explanation based on the topic so it is easy for the user to understand."
    ),
    sub_agents=[*sub_agents],
    tools=[],
)
