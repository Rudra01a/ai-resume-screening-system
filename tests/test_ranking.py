"""
Unit tests for src/ranking/.
"""
import pandas as pd


def test_rank_candidates_sorts_descending_and_assigns_rank():
    from src.ranking.ranker import rank_candidates

    feature_table = pd.DataFrame(
        {"tfidf_similarity": [0.2, 0.9, 0.5]},
        index=pd.Index(["c1", "c2", "c3"], name="candidate_id"),
    )
    scores = [0.2, 0.9, 0.5]

    ranked = rank_candidates(feature_table, scores, top_k=3)

    assert list(ranked["candidate_id"]) == ["c2", "c3", "c1"]
    assert list(ranked["rank"]) == [1, 2, 3]
