# src/similarity/

**Purpose:** Turn feature vectors into comparable scores.

| File | Responsibility |
|---|---|
| `cosine_similarity.py` | Resume-vs-JD cosine similarity over TF-IDF vectors |
| `scorer.py` | Weighted blend of similarity + skill match + (future) experience match |

Weights are pulled from `config/config.yaml` (`ranking.weights`) so the
scoring formula stays visible and tunable outside of code.
