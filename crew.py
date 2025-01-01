from crewai import Crew, Process
from agents import industry_researcher, use_case_generator, resource_collector
from tasks import industry_research_task, use_case_generation_task, resource_collection_task

ai_use_case_crew = Crew(
    agents=[industry_researcher, use_case_generator, resource_collector],
    tasks=[industry_research_task, use_case_generation_task, resource_collection_task],
    process=Process.sequential,  # or hierarchical, depending on our preference
    verbose=True
)

def ask(question):
    global ai_use_case_crew
    try:
        return ai_use_case_crew.kickoff(inputs={'company': question})
    except Exception as e:
        print(f"Error while running the task: {e}")
        return None
