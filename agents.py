from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm():
    """
    Groq LLM setup for CrewAI.

    Local .env:
    GROQ_API_KEY=your_key
    GROQ_MODEL=groq/llama-3.1-8b-instant

    Streamlit Secrets:
    GROQ_API_KEY = "your_key"
    GROQ_MODEL = "groq/llama-3.1-8b-instant"
    """

    model_name = os.getenv("GROQ_MODEL", "groq/llama-3.1-8b-instant")
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Add it in .env or Streamlit Secrets.")

    return LLM(
        model=model_name,
        api_key=api_key,
        temperature=0.1,
        max_tokens=350,
    )


def create_agents():
    llm = get_llm()

    resume_analyzer = Agent(
        role="Resume Analyzer Agent",
        goal="Review resume briefly for ATS, skills, projects, and role readiness.",
        backstory="You are a concise technical resume reviewer. Give short practical feedback.",
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=1,
    )

    job_matcher = Agent(
        role="Job Match Agent",
        goal="Compare resume with job description and give short job-fit analysis.",
        backstory="You are a concise technical recruiter. Focus only on match, gaps, and readiness.",
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=1,
    )

    final_reporter = Agent(
        role="Final Report Agent",
        goal="Combine findings into one short career report.",
        backstory="You are a concise career advisor. Produce a short markdown report.",
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=1,
    )

    return {
        "resume_analyzer": resume_analyzer,
        "job_matcher": job_matcher,
        "final_reporter": final_reporter,
    }
