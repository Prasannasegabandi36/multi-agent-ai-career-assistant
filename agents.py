from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm():
    """Create Groq LLM for CrewAI agents.

    Default model: groq/llama-3.1-8b-instant
    You can change it in .env using GROQ_MODEL.
    """
    model_name = os.getenv("GROQ_MODEL", "groq/llama-3.1-8b-instant")
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it in your .env file or Streamlit Secrets."
        )

    return LLM(
        model=model_name,
        api_key=api_key,
        temperature=0.3,
    )


def create_agents():
    llm = get_llm()

    resume_analyzer = Agent(
        role="Resume Analyzer Agent",
        goal="Analyze the candidate resume and identify strengths, weaknesses, missing keywords, and improvement opportunities.",
        backstory=(
            "You are an expert resume reviewer with experience in ATS optimization, "
            "technical resume screening, and entry-level AI/Data job applications."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    job_matcher = Agent(
        role="Job Match Agent",
        goal="Compare the resume with the job description and calculate a realistic job-fit assessment.",
        backstory=(
            "You are a technical recruiter who evaluates resumes against job descriptions "
            "and explains matched and missing skills clearly."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    skill_gap_planner = Agent(
        role="Skill Gap Planner Agent",
        goal="Create a practical learning plan based on missing skills from the resume and job description.",
        backstory=(
            "You are a career mentor who creates beginner-friendly, realistic learning roadmaps "
            "for AI, Data Science, and Data Engineering roles."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    interview_coach = Agent(
        role="Interview Coach Agent",
        goal="Generate personalized interview questions and preparation tips based on the resume and target role.",
        backstory=(
            "You are an interview coach specializing in AI, data, Python, SQL, projects, "
            "and behavioral interview preparation."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    linkedin_writer = Agent(
        role="LinkedIn Content Agent",
        goal="Create a professional LinkedIn post that summarizes the candidate's learning or project progress.",
        backstory=(
            "You are a LinkedIn personal branding expert who writes clear, professional, "
            "student-friendly posts for technology learners and job seekers."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    final_reporter = Agent(
        role="Final Career Report Agent",
        goal="Combine all analysis into one clean, structured career improvement report.",
        backstory=(
            "You are a senior career advisor who converts multiple expert reviews into "
            "one polished, easy-to-read final report."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    return {
        "resume_analyzer": resume_analyzer,
        "job_matcher": job_matcher,
        "skill_gap_planner": skill_gap_planner,
        "interview_coach": interview_coach,
        "linkedin_writer": linkedin_writer,
        "final_reporter": final_reporter,
    }
