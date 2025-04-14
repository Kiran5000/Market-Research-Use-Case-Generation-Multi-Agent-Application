from crewai import Agent, LLM
import os
from dotenv import load_dotenv
from tools import search_tool, scrape_tool, pdf_tool

load_dotenv()
together_api_key = os.getenv('TOGETHER_API_KEY')
if not together_api_key:
    raise ValueError("API key not found. Please set TOGETHER_API_KEY in your .env file.")

llm = LLM(
    model='openai/Qwen/Qwen2.5-72B-Instruct-Turbo',
    api_key=together_api_key,
    api_base='https://api.together.xyz'
)

industry_researcher = Agent(
    role="Industry Research Specialist",
    goal="""Conduct a comprehensive analysis of the {company} industry sector...""",
    backstory="""As an experienced industry analyst...""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm,
    max_rpm=20,
    max_iter=20
)

use_case_generator = Agent(
    role="AI Use Case Strategist",
    goal="""Research current and emerging industry trends within {company}'s domain...""",
    backstory="""With expertise in GenAI, AI, and ML...""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool, pdf_tool],
    llm=llm,
    max_rpm=20,
    max_retry_limit=20
)

resource_collector = Agent(
    role="AI Resource Specialist",
    goal="""Identify and compile a curated set of high-quality datasets...""",
    backstory="""An AI resource expert...""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm,
    max_rpm=20,
    max_retry_limit=20
)

print("Agents created successfully.")
