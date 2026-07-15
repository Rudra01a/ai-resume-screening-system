# tests/

Mirrors the `src/` package layout 1:1 — `test_parsing.py` tests
`src/parsing/`, etc. Run the whole suite with:

```bash
pytest tests/ -v
```

**Why this matters for this project:** the pipeline has many small, pure
functions (clean_text, extract_skills, compute_similarity...) that are
easy to unit test in isolation and easy to silently break while iterating
quickly. Tests here catch regressions before they show up as a wrong
candidate ranking in the dashboard.
