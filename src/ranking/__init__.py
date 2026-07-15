"""
ranking/  — Stage 6 of the pipeline.

WHY THIS FOLDER EXISTS:
similarity/ produces per-candidate scores; ranking/ turns that into an
ordered, decision-ready candidate list (sorted, top-K, tie-broken) - the
artifact recruiters actually consume. Separated from scorer.py so ranking
logic (sort order, filtering, top-K cutoff) can change independently of
how scores are computed.
"""
