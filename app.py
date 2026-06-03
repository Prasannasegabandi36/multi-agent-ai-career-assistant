import os
import streamlit as st
from dotenv import load_dotenv

from crew_runner import run_career_crew
from utils import extract_text_from_pdf, save_report, load_sample_file

load_dotenv()

st.set_page_config(
    page_title="Multi-Agent AI Career Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Multi-Agent AI Career Assistant")
st.caption("Built with CrewAI + Groq API + Streamlit")

with st.sidebar:
    st.header("Project Info")
    st.write("This app uses multiple AI agents to analyze resume, job description, skills, and interview preparation.")
    st.markdown("""
    **Agents used:**
    - Resume Analyzer
    - Job Match Agent
    - Skill Gap Planner
    - Interview Coach
    - LinkedIn Content Agent
    - Final Report Agent
    """)

    st.divider()
    st.subheader("Groq API Status")
    if os.getenv("GROQ_API_KEY"):
        st.success("GROQ_API_KEY found")
    else:
        st.error("GROQ_API_KEY missing")
        st.info("Add your key in .env locally or Streamlit Secrets when deployed.")

st.subheader("1. Enter Candidate Details")

col1, col2 = st.columns(2)

with col1:
    candidate_name = st.text_input("Candidate Name", value="Prasanna")

with col2:
    target_role = st.text_input("Target Role", value="AI Engineer Intern")

st.subheader("2. Add Resume")

resume_input_method = st.radio(
    "Choose resume input method",
    ["Paste resume text", "Upload PDF", "Use sample resume"],
    horizontal=True,
)

resume_text = ""

if resume_input_method == "Paste resume text":
    resume_text = st.text_area("Paste resume text here", height=220)
elif resume_input_method == "Upload PDF":
    uploaded_resume = st.file_uploader("Upload resume PDF", type=["pdf"])
    if uploaded_resume:
        try:
            resume_text = extract_text_from_pdf(uploaded_resume)
            st.success("Resume PDF text extracted successfully")
            with st.expander("Preview extracted resume text"):
                st.write(resume_text[:3000])
        except Exception as e:
            st.error(str(e))
else:
    resume_text = load_sample_file("data/sample_resume.txt")
    st.text_area("Sample resume", value=resume_text, height=220)

st.subheader("3. Add Job Description")

job_input_method = st.radio(
    "Choose job description input method",
    ["Paste job description", "Use sample job description"],
    horizontal=True,
)

if job_input_method == "Paste job description":
    job_description = st.text_area("Paste job description here", height=220)
else:
    job_description = load_sample_file("data/sample_job_description.txt")
    st.text_area("Sample job description", value=job_description, height=220)

st.subheader("4. Run Multi-Agent Analysis")

run_button = st.button("🚀 Run CrewAI Agents", type="primary")

if run_button:
    if not os.getenv("GROQ_API_KEY"):
        st.error("Please add GROQ_API_KEY before running the app.")
    elif not resume_text.strip():
        st.error("Please provide resume text or upload a resume PDF.")
    elif not job_description.strip():
        st.error("Please provide a job description.")
    else:
        with st.spinner("CrewAI agents are working on your career report..."):
            try:
                final_report = run_career_crew(
                    resume_text=resume_text,
                    job_description=job_description,
                    target_role=target_role,
                )

                report_path = save_report(final_report)

                st.success("Multi-agent analysis completed!")
                st.subheader("📄 Final Career Report")
                st.markdown(final_report)

                st.download_button(
                    label="⬇️ Download Report as Markdown",
                    data=final_report,
                    file_name="multi_agent_career_report.md",
                    mime="text/markdown",
                )

                st.info(f"Report also saved locally at: {report_path}")

            except Exception as e:
                st.error("Something went wrong while running the agents.")
                st.exception(e)

st.divider()
st.markdown("""
### Resume Project Title
**Multi-Agent AI Career Assistant using CrewAI and Groq LLM API**

### Resume Bullet
Built a multi-agent AI Career Assistant using CrewAI, Groq LLM API, Python, and Streamlit to analyze resumes, compare job descriptions, identify skill gaps, generate interview questions, and create personalized career reports.
""")
