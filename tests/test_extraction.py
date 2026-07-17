from src.extraction.skill_extractor import extract_skills


def test_extract_skills_finds_known_skills():
    text = """
    Python developer with experience in TensorFlow,
    Machine Learning, Git, Docker and AWS.
    """

    skills = extract_skills(text)

    assert "python" in skills
    assert "tensorflow" in skills
    assert "machine learning" in skills
    assert "git" in skills