# scripts/

Orchestration entrypoints — the "glue" that wires `src/` modules into a
runnable pipeline. This is deliberately separate from `src/` itself: the
domain logic in `src/` stays reusable and side-effect-free (pure
functions), while `scripts/` is where side effects (reading files,
writing outputs, printing logs) are allowed to happen.

| File | Responsibility |
|---|---|
| `run_pipeline.py` | End-to-end: parse -> preprocess -> extract -> score -> rank -> report |
| `setup_env.sh` | One-time environment bootstrap (venv, deps, NLTK/spaCy downloads) |
