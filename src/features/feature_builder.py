"""
Combines multiple feature signals (TF-IDF similarity, skill overlap, etc.)
into a single feature table — one row per candidate — that ranking/ can
consume. This is the module that would grow if new signals (e.g. years of
experience, embeddings) are added later.
"""
import pandas as pd


def build_feature_table(candidate_ids: list[str], tfidf_scores: list[float],
                         skill_match_scores: list[float]) -> pd.DataFrame:
    """
    Assemble a per-candidate feature DataFrame.

    Args:
        candidate_ids: identifiers (e.g. filenames) for each candidate.
        tfidf_scores: cosine similarity score per candidate vs the JD.
        skill_match_scores: fraction of required skills matched per candidate.

    Returns:
        DataFrame indexed by candidate_id with one column per feature.
    """
    return pd.DataFrame({
        "candidate_id": candidate_ids,
        "tfidf_similarity": tfidf_scores,
        "skill_match": skill_match_scores,
    }).set_index("candidate_id")
