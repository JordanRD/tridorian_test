from google.adk.agents.llm_agent import LlmAgent
from ..tools.fmp_tools import fmp_tools


fmp_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fmp_agent",
    description="This agent provides access to multiple tools for analyzing stock market data. It allows you to fetch real-time stock prices, company profiles, peer companies, exchange market hours, and search for companies by name. The agent integrates with an underlying market data API to provide up-to-date financial information and metadata for listed companies and exchanges.",
    instruction="Use the available tools to fetch stock and market data. When tool failing, Please inform the user and suggest to alternatives, like manual searches. Never exposes sensitive information like API keys.",
    tools=fmp_tools,
)
