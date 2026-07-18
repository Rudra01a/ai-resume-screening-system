"""
Compute skill-match scores between extracted resume skills and
required job description skills.
"""


def compute_skill_match(
    resume_skills: list[str],
    required_skills: list[str],
) -> float:
    """
    Compute the fraction of required skills present in a resume.

    Args:
        resume_skills: Skills extracted from a candidate's resume.
        required_skills: Skills required for the job.

    Returns:
        A score between 0.0 and 1.0.
    """
    if not required_skills:
        return 0.0

    resume_set = {skill.lower().strip() for skill in resume_skills}
    required_set = {skill.lower().strip() for skill in required_skills}

    matched = resume_set.intersection(required_set)

    return len(matched) / len(required_set)