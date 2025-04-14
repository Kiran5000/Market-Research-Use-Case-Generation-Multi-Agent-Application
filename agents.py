import streamlit as st
from crewai import Agent, LLM
from tools import search_tool, scrape_tool, pdf_tool

llm = LLM(
    model='openai/Qwen/Qwen2.5-72B-Instruct-Turbo',
    api_key=st.secrets["TOGETHER_API_KEY"],
    api_base='https://api.together.xyz'
)

industry_researcher = Agent(
    role="Industry Research Specialist",
    goal="Conduct detailed market analysis and trends for {company}.",
    backstory="A seasoned analyst with insights into market trends and competition.",
    tools=[search_tool, scrape_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

use_case_generator = Agent(
    role="AI Use Case Strategist",
    goal="Generate AI/ML use cases to benefit {company}.",
    backstory="You bridge tech advancements with business use cases.",
    tools=[search_tool, scrape_tool, pdf_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

resource_collector = Agent(
    role="AI Resource Specialist",
    goal="Find datasets and libraries to support AI use cases for {company}.",
    backstory="An expert at sourcing practical and scalable AI tools.",
    tools=[search_tool, scrape_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)
