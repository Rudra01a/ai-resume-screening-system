"""
Compute cosine similarity between candidate resume vectors and a job
description vector.
"""
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(resume_matrix, jd_vector) -> list[float]:
    """
    Args:
        resume_matrix: TF-IDF matrix of shape (n_candidates, n_features).
        jd_vector: TF-IDF vector of shape (1, n_features) for the job description.

    Returns:
        List of similarity scores (0.0-1.0), one per candidate, in the
        same order as resume_matrix rows.
    """
    scores = cosine_similarity(resume_matrix, jd_vector)
    return scores.flatten().tolist()
