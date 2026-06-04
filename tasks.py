from crewai import Task


def create_tasks(agents, resume_text, job_description, target_role):
    resume_task = Task(
        description=f"""
Analyze the resume for the target role: {target_role}.

Resume:
{resume_text[:2500]}

Give a concise resume review.

Include only:
1. Resume summary in 3 lines
2. Top 5 strengths
3. Top 5 improvements
4. Missing ATS keywords
5. Resume score out of 100

Keep the answer short and practical.
""",
        expected_output=(
            "A concise resume analysis with summary, strengths, improvements, missing keywords, and score."
        ),
        agent=agents["resume_analyzer"],
    )

    job_match_task = Task(
        description=f"""
Compare the resume with the job description for the target role: {target_role}.

Resume:
{resume_text[:2500]}

Job Description:
{job_description[:2000]}

Give a concise job match report.

Include only:
1. Match percentage
2. Matched skills
3. Missing skills
4. Experience gaps
5. Hiring readiness: Low / Medium / High

Keep the answer short and practical.
""",
        expected_output=(
            "A concise job match report with match percentage, matched skills, missing skills, gaps, and readiness level."
        ),
        agent=agents["job_matcher"],
        context=[resume_task],
    )

    final_report_task = Task(
        description=f"""
Create one final career improvement report for the target role: {target_role}.

Use the previous agent outputs.

Final report format:

# Multi-Agent AI Career Report

## 1. Candidate Summary
Write 3-4 lines.

## 2. Resume Analysis
Summarize resume score, strengths, and improvements.

## 3. Job Match Analysis
Summarize match percentage, matched skills, missing skills, and readiness level.

## 4. 7-Day Skill Improvement Plan
Give a short 7-day plan only.

## 5. Interview Preparation
Give 5 technical questions and 3 HR questions.

## 6. Final Recommendations
Give 5 clear recommendations.

Keep the report professional, concise, and resume-project friendly.
""",
        expected_output=(
            "A final markdown career report with resume analysis, job match, 7-day plan, interview questions, and recommendations."
        ),
        agent=agents["final_reporter"],
        context=[resume_task, job_match_task],
    )

    return [
        resume_task,
        job_match_task,
        final_report_task,
    ]
