# Multi-Agent AI Career Assistant using CrewAI and Groq

A professional Streamlit web application that uses a **CrewAI multi-agent workflow** and **Groq LLM API** to analyze resumes, compare job descriptions, identify skill gaps, generate interview questions, and create a final career improvement report.

---

## 🔗 Project Links

* **Live Streamlit App:** https://multi-agent-ai-career-assistant.streamlit.app/
* **GitHub Repository:** https://github.com/Prasannasegabandi36/multi-agent-ai-career-assistant
* **GitHub Profile:** https://github.com/Prasannasegabandi36

---

## 🚀 Project Overview

The **Multi-Agent AI Career Assistant** is an agentic AI project designed to help students, freshers, and job seekers understand how well their resume matches a target job role.

Instead of using a simple chatbot, this project uses a structured multi-agent workflow where each agent has a specific responsibility. The agents work together to review the resume, compare it with a job description, and generate a clear career improvement report.

This project demonstrates practical knowledge of:

* Agentic AI
* CrewAI
* LLM API integration
* Streamlit application development
* Resume and job description analysis
* Modular Python project structure
* Cloud deployment using Streamlit Cloud

---

## 🎯 Problem Statement

Many students and job seekers struggle to understand:

* Whether their resume matches a job description
* Which skills are missing for a target role
* How to improve their resume for ATS screening
* What interview questions they should prepare
* How ready they are for a specific job role

This project solves the problem by using multiple AI agents to generate structured, role-specific career guidance.

---

## 🧠 Agents Used

The current optimized version uses **3 CrewAI agents** to reduce Groq free-tier token usage and avoid rate-limit errors.

### 1. Resume Analyzer Agent

Reviews the candidate resume and provides:

* Resume summary
* Strengths
* Improvement points
* Missing ATS keywords
* Resume score

### 2. Job Match Agent

Compares the resume with the job description and provides:

* Match percentage
* Matched skills
* Missing skills
* Readiness level

### 3. Final Career Report Agent

Combines all findings into one structured report containing:

* Candidate summary
* Resume feedback
* Job match analysis
* 7-day improvement plan
* Interview questions
* Final recommendations

---

## 🏗️ Multi-Agent Workflow

```text
User Input
   ↓
Streamlit Frontend
   ↓
CrewAI Sequential Workflow
   ↓
Resume Analyzer Agent
   ↓
Job Match Agent
   ↓
Final Career Report Agent
   ↓
Final Career Improvement Report
```

---

## ✅ Features

* Resume text input
* Resume PDF upload support
* Job description text input
* Sample resume option
* Sample job description option
* Target role selection
* CrewAI multi-agent workflow
* Resume analysis
* Job match analysis
* Skill gap identification
* ATS-style feedback
* 7-day improvement plan
* Interview question generation
* Final markdown career report
* Downloadable report
* Streamlit Cloud deployment

---

## 🛠️ Tech Stack

| Category              | Tools Used           |
| --------------------- | -------------------- |
| Programming Language  | Python               |
| AI Agent Framework    | CrewAI               |
| LLM Provider          | Groq API             |
| LLM Model             | Llama 3.1 Groq Model |
| Frontend              | Streamlit            |
| PDF Processing        | pypdf                |
| Environment Variables | python-dotenv        |
| Version Control       | Git and GitHub       |
| Deployment            | Streamlit Cloud      |

---

## 📂 Folder Structure

```text
multi-agent-ai-career-assistant/
│
├── app.py
├── agents.py
├── tasks.py
├── crew_runner.py
├── utils.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── data/
│   ├── sample_resume.txt
│   └── sample_job_description.txt
│
├── outputs/
│   └── .gitkeep
│
└── screenshots/
    └── .gitkeep
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Prasannasegabandi36/multi-agent-ai-career-assistant.git
cd multi-agent-ai-career-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install requirements

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root folder.

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=groq/llama-3.1-8b-instant
```

Important:

```text
Do not upload your real .env file to GitHub.
Only upload .env.example.
```

---

## ▶️ Run the App Locally

```bash
streamlit run app.py
```

After running, open the local URL shown in your terminal.

Usually:

```text
http://localhost:8501
```

---

## 🌐 Streamlit Cloud Deployment

To deploy this project on Streamlit Cloud:

1. Push all project files to GitHub.
2. Open Streamlit Cloud.
3. Click **New app**.
4. Select this repository:

```text
Prasannasegabandi36/multi-agent-ai-career-assistant
```

5. Set main file path:

```text
app.py
```

6. Add this in **Secrets**:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
GROQ_MODEL = "groq/llama-3.1-8b-instant"
```

7. Click **Deploy**.

---

## 🧪 Sample Resume Input

```text
Python and SQL beginner with projects in Streamlit, AWS S3, and data analysis. Built AI Shopping Assistant, Tuition Manager, and data dashboard projects. Skills include Python, Pandas, SQL, GitHub, Streamlit, AWS basics, and machine learning basics.
```

---

## 🧪 Sample Job Description

```text
Data Engineer role requiring Python, SQL, AWS, ETL pipelines, Snowflake, PySpark, Git, data quality checks, and dashboard reporting.

Responsibilities:
- Build and maintain ETL data pipelines.
- Write SQL queries for data cleaning and transformation.
- Work with AWS S3, Glue, Lambda, and CloudWatch.
- Use Snowflake for data storage and reporting.
- Create basic PySpark jobs for large datasets.
- Add data quality checks and error handling.

Required Skills:
Python, SQL, AWS, Snowflake, PySpark, ETL, Git, data modeling.

Preferred Skills:
Airflow, dbt, Kafka, Databricks, Power BI.
```

---

## 📊 Output Generated

The application generates a structured career report including:

* Candidate summary
* Resume feedback
* Resume strengths
* Resume improvement points
* Job match percentage
* Missing skills
* 7-day learning plan
* Interview questions
* Final recommendations

---

## 📸 Screenshots

Add your Streamlit dashboard screenshots inside the `screenshots/` folder after running the app.

Suggested screenshots:

```text
screenshots/homepage.png
screenshots/input_form.png
screenshots/final_report.png
```

After uploading screenshots, you can display them like this:

```md
![Homepage](screenshots/homepage.png)
![Final Report](screenshots/final_report.png)
```

---

## 📌 Resume Bullet Point

```text
Built a multi-agent AI Career Assistant using CrewAI, Groq LLM API, Python, and Streamlit to analyze resumes, compare job descriptions, identify skill gaps, generate interview questions, and create personalized career reports.
```

---

## 💼 Resume Project Title

```text
Multi-Agent AI Career Assistant using CrewAI and Groq
```

---

## 🔍 Skills Demonstrated

This project demonstrates hands-on experience in:

* Python application development
* Agentic AI workflow design
* CrewAI multi-agent orchestration
* LLM API integration using Groq
* Streamlit frontend development
* Resume and job description analysis
* Prompt engineering
* Modular code organization
* GitHub project documentation
* Cloud deployment

---

## 🚧 Rate Limit Note

Groq free/on-demand tier may have token-per-minute limits. To avoid rate-limit errors:

* Use short resume input while testing
* Use short job descriptions
* Wait 30–60 seconds between runs
* Keep output concise
* Use fewer agents in the workflow

The current version is optimized with 3 agents to reduce token usage.

---

## 🔮 Future Improvements

* Add PDF report export
* Add ATS keyword dashboard
* Add job search API integration
* Add LinkedIn post generation agent
* Add skill roadmap generation agent
* Add n8n automation for email reports
* Add Guardrails for structured output validation
* Add Ollama local model support
* Add MCP integration for Google Drive and GitHub
* Add user authentication
* Add multiple resume comparison feature

---

## 👩‍💻 Author

**Prasanna**

* GitHub: https://github.com/Prasannasegabandi36
* Live Project: https://multi-agent-ai-career-assistant.streamlit.app/
* Project Repository: https://github.com/Prasannasegabandi36/multi-agent-ai-career-assistant

---

## 📄 License

This project is created for learning, portfolio building, and resume demonstration purposes.
