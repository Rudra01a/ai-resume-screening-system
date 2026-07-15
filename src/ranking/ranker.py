"""
Sort candidates by weighted score and return the final ranked list.
"""
import pandas as pd


def rank_candidates(feature_table: pd.DataFrame, scores: list[float], top_k: int = 20) -> pd.DataFrame:
    """
    Args:
        feature_table: DataFrame indexed by candidate_id (from features/feature_builder.py).
        scores: weighted composite score per candidate, same order as feature_table rows.
        top_k: number of top candidates to return.

    Returns:
        DataFrame sorted by score descending, with a "rank" column added,
        truncated to top_k rows.
    """
    result = feature_table.copy()
    result["final_score"] = scores
    result = result.sort_values("final_score", ascending=False).reset_index()
    result.insert(0, "rank", range(1, len(result) + 1))
    return result.head(top_k)
