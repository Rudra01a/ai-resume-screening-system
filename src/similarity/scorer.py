"""
Combine similarity and skill-match signals into a single weighted score
using weights defined in src/config.py.
"""
from src.config import TFIDF_WEIGHT, SKILL_WEIGHT

def compute_weighted_score(tfidf_similarity: float, skill_match: float,
                            experience_match: float = 0.0,
                            weights: dict | None = None) -> float:
    """
    Args:
        tfidf_similarity: cosine similarity score (0-1).
        skill_match: fraction of required skills present (0-1).
        experience_match: normalized experience-fit score (0-1), optional.
        weights: dict with keys tfidf_similarity/skill_match/experience_match;
                  defaults to config/config.yaml's `ranking.weights` values.

    Returns:
        Weighted composite score (0-1).
    """
    if weights is None:
        weights = {
        "tfidf_similarity": TFIDF_WEIGHT,
        "skill_match": SKILL_WEIGHT,
        "experience_match": 0.0,
    }
    return (
        weights["tfidf_similarity"] * tfidf_similarity
        + weights["skill_match"] * skill_match
        + weights["experience_match"] * experience_match
    )
