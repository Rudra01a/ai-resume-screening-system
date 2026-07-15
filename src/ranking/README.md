# src/ranking/

**Purpose:** Turn per-candidate scores into the final, sorted candidate
list that gets shown on the dashboard and exported in reports.

| File | Responsibility |
|---|---|
| `weighting.py` | Loads + validates ranking weights from `config/config.yaml` |
| `ranker.py` | Sorts candidates by weighted score, assigns rank, truncates to top-K |
