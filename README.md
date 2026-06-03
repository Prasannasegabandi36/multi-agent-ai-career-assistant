# Multi-Agent AI Career Assistant using CrewAI and Groq

A Streamlit web application that uses **CrewAI multi-agent workflow** and **Groq LLM API** to analyze resumes, compare job descriptions, identify skill gaps, generate interview questions, and create a final career improvement report.

## 🚀 Project Overview

This project demonstrates an agentic AI system where multiple specialized agents collaborate to complete a career guidance workflow.

## 🧠 Agents Used

1. **Resume Analyzer Agent**  
   Reviews resume strengths, weaknesses, ATS keywords, and improvement points.

2. **Job Match Agent**  
   Compares resume with job description and provides job-fit analysis.

3. **Skill Gap Planner Agent**  
   Creates a practical learning roadmap based on missing skills.

4. **Interview Coach Agent**  
   Generates technical, project, HR, and scenario-based interview questions.

5. **LinkedIn Content Agent**  
   Creates a professional LinkedIn post for career/project progress.

6. **Final Career Report Agent**  
   Combines all outputs into one structured final report.

## 🛠️ Tech Stack

- Python
- CrewAI
- Groq API
- Streamlit
- pypdf
- python-dotenv
- GitHub
- Streamlit Cloud

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

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/multi-agent-ai-career-assistant.git
cd multi-agent-ai-career-assistant
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Add Groq API key

Create a `.env` file in the root folder:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=groq/llama-3.1-8b-instant
```

Do not upload `.env` to GitHub.

### 5. Run the app

```bash
streamlit run app.py
```

## 🌐 Streamlit Cloud Deployment

When deploying on Streamlit Cloud:

1. Push all files to GitHub.
2. Open Streamlit Cloud.
3. Create a new app from your GitHub repo.
4. Add this in **Secrets**:

```toml
GROQ_API_KEY="your_groq_api_key_here"
GROQ_MODEL="groq/llama-3.1-8b-instant"
```

5. Deploy the app.

## ✅ Features

- Resume text input
- Resume PDF upload
- Job description input
- Target role selection
- Multi-agent CrewAI workflow
- Resume analysis
- Job match analysis
- Skill gap roadmap
- Interview preparation questions
- LinkedIn post generation
- Downloadable final markdown report

## 📌 Resume Bullet Point

Built a multi-agent AI Career Assistant using CrewAI, Groq LLM API, Python, and Streamlit to analyze resumes, compare job descriptions, identify skill gaps, generate interview questions, and create personalized career reports.

## 🔮 Future Improvements

- Add PDF report export
- Add ATS keyword visual dashboard
- Add job search API integration
- Add n8n automation for email reports
- Add Guardrails for output validation
- Add Ollama local model support
- Add MCP integration for Google Drive/GitHub

## 📸 Screenshots

Add your Streamlit dashboard screenshots inside the `screenshots/` folder after running the app.
