"""
Resume Vector Matchers and Mock Interview Question Generators
"""

def compute_resume_similarity(resume_skills: list, job_skills: list) -> float:
    overlap = set(resume_skills).intersection(set(job_skills))
    return len(overlap) / max(len(job_skills), 1)