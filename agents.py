from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm():
    """
    Create Groq LLM for CrewAI agents.

    Required in .env or Streamlit Secrets:
    GROQ_API_KEY=your_groq_api_key
    GROQ_MODEL=groq/llama-3.1-8b-instant
    """

    model_name = os.getenv("GROQ_MODEL", "groq/llama-3.1-8b-instant")
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it in your .env file locally or Streamlit Secrets in cloud."
        )

    return LLM(
        model=model_name,
        api_key=api_key,
        temperature=0.2,
        max_tokens=700,
    )


def create_agents():
    llm = get_llm()

    resume_analyzer = Agent(
        role="Resume Analyzer Agent",
        goal=(
            "Analyze the candidate resume for the target role and provide concise ATS-style feedback."
        ),
        backstory=(
            "You are an expert technical resume reviewer. You check resumes for ATS keywords, "
            "skills, project quality, clarity, and role readiness. You give short, practical feedback."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=1,
    )

    job_matcher = Agent(
        role="Job Match Agent",
        goal=(
            "Compare the resume with the job description and provide a short job-fit analysis."
        ),
        backstory=(
            "You are a technical recruiter. You compare resumes with job descriptions and identify "
            "matched skills, missing skills, and readiness level in a clear and concise way."
        ),
        llm=llm,
        verbose=False,
        allow_delegation=False,
        max_iter=1,
    )

    final_reporter = Agent(
        role="Final Career Report Agent",
        goal=(
            "Create one clean final career report using the resume analysis and job match findings."
        ),
        backstory=(
            "You are a senior career advisor. You combine agent outputs into a polished, readable, "
            "student-friendly career improvement report."
        ),
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
