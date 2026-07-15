# src/bias_detection/  (roadmap — not yet implemented)

**Intended purpose:** Audit `ranking/` output for fairness issues before
it reaches a recruiter — e.g. checking whether the model systematically
scores certain groups lower, given resume features that correlate with
protected attributes.

**Suggested approach when implemented:** load the ranked DataFrame from
`ranking/ranker.py`, join with any available demographic proxy signals,
and compute standard fairness metrics (e.g. via the `fairlearn` library —
already listed, commented out, in `requirements.txt`). Surface results in
`frontend/pages/` as a dedicated "Fairness Audit" page.
