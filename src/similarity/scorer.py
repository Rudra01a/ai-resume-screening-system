"""
Combine similarity + skill-match signals into a single weighted score per
candidate, using weights from config/config.yaml.
"""


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
        weights = {"tfidf_similarity": 0.6, "skill_match": 0.3, "experience_match": 0.1}

    return (
        weights["tfidf_similarity"] * tfidf_similarity
        + weights["skill_match"] * skill_match
        + weights["experience_match"] * experience_match
    )
