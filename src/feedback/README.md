# src/feedback/  (roadmap — not yet implemented)

**Intended purpose:** Close the loop between recruiter decisions and the
model. When a recruiter marks a ranked candidate as a good/bad fit, that
signal should feed back into either:

1. `ranking/weighting.py` — nudge the TF-IDF/skill-match weight balance, or
2. A future learned ranker (e.g. gradient-boosted re-ranker trained on
   accumulated feedback) that replaces the fixed-weight formula.

**Suggested storage:** a simple `data/processed/feedback.csv`
(candidate_id, job_id, recruiter_label, timestamp) is enough to start —
no separate database needed until volume demands it.
