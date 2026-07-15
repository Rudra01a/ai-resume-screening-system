"""
Unit tests for src/similarity/.
"""


def test_compute_weighted_score_default_weights():
    from src.similarity.scorer import compute_weighted_score

    score = compute_weighted_score(tfidf_similarity=1.0, skill_match=1.0, experience_match=1.0)
    assert abs(score - 1.0) < 1e-9


def test_compute_weighted_score_zero_inputs():
    from src.similarity.scorer import compute_weighted_score

    score = compute_weighted_score(tfidf_similarity=0.0, skill_match=0.0)
    assert score == 0.0
