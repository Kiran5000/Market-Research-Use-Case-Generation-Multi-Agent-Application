from crewai import Task
from agents import industry_researcher, use_case_generator, resource_collector

industry_research_task = Task(
    description="Perform market analysis, identify trends, and evaluate competitors for {company}.",
    expected_output=(
        "1. Industry overview\n"
        "2. Key offerings\n"
        "3. Strategic areas\n"
        "4. Competitors\n"
        "5. Trends\n"
        "6. Challenges and opportunities"
    ),
    agent=industry_researcher
)

use_case_generation_task = Task(
    description="Research AI/ML use cases for {company} and propose practical implementations.",
    expected_output=(
        "List 4–5 use cases with:\n"
        "1. Objective\n"
        "2. Implementation approach\n"
        "3. Libraries or frameworks\n"
        "4. Cross-department benefits"
    ),
    agent=use_case_generator
)

resource_collection_task = Task(
    description="Identify high-quality datasets/tools for each use case of {company}.",
    expected_output=(
        "For each use case:\n"
        "1. Brief description\n"
        "2. Tools/libraries\n"
        "3. 2-3 relevant dataset links"
    ),
    agent=resource_collector
)
