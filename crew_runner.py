from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks


def run_career_crew(resume_text: str, job_description: str, target_role: str) -> str:
    """Run the CrewAI multi-agent workflow and return the final report."""

    agents = create_agents()
    tasks = create_tasks(agents, resume_text, job_description, target_role)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff()
    return str(result)
