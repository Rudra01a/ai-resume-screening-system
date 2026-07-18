from src.similarity.skill_match import compute_skill_match


def test_compute_skill_match():
    resume_skills = [
        "python",
        "tensorflow",
        "git",
        "docker",
    ]

    required_skills = [
        "python",
        "tensorflow",
        "sql",
        "git",
    ]

    score = compute_skill_match(
        resume_skills,
        required_skills,
    )

    assert score == 0.75


def test_empty_required_skills():
    assert compute_skill_match(["python"], []) == 0.0