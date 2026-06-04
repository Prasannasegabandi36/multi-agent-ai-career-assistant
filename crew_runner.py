from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks
import time


def run_career_crew(resume_text: str, job_description: str, target_role: str) -> str:
    """Run CrewAI workflow and return final report."""

    agents = create_agents()
    tasks = create_tasks(agents, resume_text, job_description, target_role)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=False,
        step_callback=lambda step: time.sleep(3),
    )

    try:
        result = crew.kickoff()
        return str(result)

    except Exception as e:
        error_message = str(e)

        if "RateLimitError" in error_message or "rate_limit_exceeded" in error_message:
            return """
# Groq Rate Limit Reached

Your app is working, but Groq free tier token limit was reached.

Please wait 30–60 seconds and run again with shorter resume/job description.

For best testing:
- Resume: under 10 lines
- Job description: under 10 lines
- Wait 1 minute between runs
"""

        return f"""
# Error Running Agents

Something went wrong:

{error_message}
"""
