from crewai import Task


def create_tasks(agents, resume_text, job_description, target_role):
    resume_short = resume_text[:1200]
    jd_short = job_description[:900]

    resume_task = Task(
        description=f"""
Target role: {target_role}

Resume:
{resume_short}

Give short resume review only.

Format:
- Summary: 2 lines
- Strengths: 3 bullets
- Improvements: 3 bullets
- Missing keywords: 5 words max
- Score: /100

Keep under 180 words.
""",
        expected_output="Short resume review under 180 words.",
        agent=agents["resume_analyzer"],
    )

    job_match_task = Task(
        description=f"""
Target role: {target_role}

Resume:
{resume_short}

Job Description:
{jd_short}

Give short job match analysis only.

Format:
- Match percentage
- Matched skills: 5 max
- Missing skills: 5 max
- Readiness: Low/Medium/High

Keep under 160 words.
""",
        expected_output="Short job match report under 160 words.",
        agent=agents["job_matcher"],
        context=[resume_task],
    )

    final_report_task = Task(
        description=f"""
Create final short career report for: {target_role}

Use previous outputs only.

Format:
# Multi-Agent AI Career Report

## Candidate Summary
3 lines max.

## Resume Feedback
3 bullets max.

## Job Match
3 bullets max.

## 7-Day Plan
Day 1 to Day 7, one short line each.

## Interview Questions
5 technical questions only.

## Final Recommendations
3 bullets max.

Keep total report under 350 words.
""",
        expected_output="Final markdown career report under 350 words.",
        agent=agents["final_reporter"],
        context=[resume_task, job_match_task],
    )

    return [resume_task, job_match_task, final_report_task]
