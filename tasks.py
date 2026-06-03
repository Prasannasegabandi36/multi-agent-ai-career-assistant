from crewai import Task


def create_tasks(agents, resume_text, job_description, target_role):
    resume_task = Task(
        description=f"""
Analyze the resume for the target role: {target_role}.

Resume:
{resume_text}

Provide:
1. Resume summary
2. Strong points
3. Weak points
4. Missing ATS keywords
5. 5 improved resume bullet points
6. Overall resume score out of 100
""",
        expected_output="A structured resume analysis with score, strengths, weaknesses, missing keywords, and improved bullet points.",
        agent=agents["resume_analyzer"],
    )

    job_match_task = Task(
        description=f"""
Compare the resume with this job description for the target role: {target_role}.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:
1. Match percentage
2. Matched skills
3. Missing skills
4. Experience gaps
5. Role-fit explanation
6. Final hiring readiness level: Low / Medium / High
""",
        expected_output="A job match report with percentage, matched skills, missing skills, and hiring readiness level.",
        agent=agents["job_matcher"],
        context=[resume_task],
    )

    skill_gap_task = Task(
        description=f"""
Create a 14-day practical learning plan for the candidate based on the resume, job description, and target role: {target_role}.

Resume:
{resume_text}

Job Description:
{job_description}

The plan should include:
1. Daily topic
2. Practice task
3. Mini project idea if useful
4. GitHub update suggestion
5. LinkedIn update suggestion
""",
        expected_output="A 14-day beginner-friendly skill gap learning roadmap.",
        agent=agents["skill_gap_planner"],
        context=[resume_task, job_match_task],
    )

    interview_task = Task(
        description=f"""
Prepare interview questions for the target role: {target_role}.

Use the candidate resume and job description.

Provide:
1. 10 technical questions
2. 5 project explanation questions
3. 5 HR/behavioral questions
4. 5 scenario-based questions
5. Short answer tips for the candidate
""",
        expected_output="A personalized interview preparation question bank with answer tips.",
        agent=agents["interview_coach"],
        context=[resume_task, job_match_task],
    )

    linkedin_task = Task(
        description=f"""
Write a professional LinkedIn post for the candidate about improving career readiness for {target_role}.

The post should mention:
1. Resume improvement
2. Skill gap learning
3. Interview preparation
4. Multi-agent AI project usage if relevant
5. 5 suitable hashtags

Keep it professional and student-friendly.
""",
        expected_output="A polished LinkedIn post with hashtags.",
        agent=agents["linkedin_writer"],
        context=[resume_task, job_match_task, skill_gap_task],
    )

    final_report_task = Task(
        description=f"""
Create one final career improvement report for the target role: {target_role}.

Combine all previous agent outputs into a clean report with these sections:

# Multi-Agent AI Career Report

## 1. Candidate Summary
## 2. Resume Analysis
## 3. Job Match Analysis
## 4. Skill Gap Roadmap
## 5. Interview Preparation
## 6. LinkedIn Post
## 7. Final Recommendations

Make it clear, structured, and ready to download.
""",
        expected_output="A complete final career report in markdown format.",
        agent=agents["final_reporter"],
        context=[resume_task, job_match_task, skill_gap_task, interview_task, linkedin_task],
    )

    return [
        resume_task,
        job_match_task,
        skill_gap_task,
        interview_task,
        linkedin_task,
        final_report_task,
    ]
