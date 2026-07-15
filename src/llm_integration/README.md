# src/llm_integration/  (roadmap — not yet implemented)

**Intended purpose:**
- Generate a plain-English explanation of each candidate's score
  ("ranked #2 because of strong TF-IDF overlap on 'React' and 'Node.js',
  but missing 'AWS' from required skills").
- Optionally re-rank the top-K candidates from `ranking/ranker.py` using
  an LLM call for cases where lexical similarity (TF-IDF) misses
  semantic matches ("built ML models" ≈ "developed machine learning
  systems").

**Suggested entrypoint when implemented:** `explain_ranking(candidate_row, job_description) -> str`,
called from `frontend/pages/3_Ranking_Dashboard.py` per selected candidate,
using the Anthropic API pattern already available in this environment
(`anthropic>=0.25.0`, commented out in `requirements.txt` until needed).
