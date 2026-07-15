# Architecture

## Layering (clean architecture)

```
frontend/        <- presentation (Streamlit) - depends on scripts/ and src/
scripts/          <- orchestration - wires src/ modules into an end-to-end run
src/              <- domain logic (parsing -> preprocessing -> extraction ->
                     features -> similarity -> ranking -> reporting)
config/, utils/    <- cross-cutting concerns used by every layer above
```

**Dependency rule:** arrows only point downward. `src/parsing` never
imports from `frontend/`; `frontend/` may import from `src/` and
`scripts/`. This is what makes the domain layer (the actual NLP/ML work)
independently testable and reusable outside Streamlit.

## Pipeline stages (in order)

1. **Parsing** (`src/parsing/`) — PDF/DOCX -> raw text
2. **Preprocessing** (`src/preprocessing/`) — raw text -> clean/tokenized text
3. **Extraction** (`src/extraction/`) — clean text -> skills, entities, sections
4. **Features** (`src/features/`) — text -> TF-IDF vectors
5. **Similarity** (`src/similarity/`) — vectors -> per-candidate similarity score
6. **Ranking** (`src/ranking/`) — scores -> sorted, top-K candidate list
7. **Reporting** (`src/reporting/`) — ranked list -> PDF/CSV report
8. **Frontend** (`frontend/`) — Streamlit dashboard over steps 1-7

## Roadmap extension points

| Roadmap item | Where it plugs in |
|---|---|
| Named Entity Recognition | `src/extraction/entity_extractor.py` (baseline already functional) |
| LLM integration | `src/llm_integration/` (new package, calls existing `ranking/` output) |
| Bias detection | `src/bias_detection/` (new package, consumes `ranking/` output) |
| Recruiter feedback loop | `src/feedback/` (new package, writes back into `ranking/weighting.py`) |
| Dense embeddings | `src/features/embeddings.py` (same interface as `tfidf_features.py`) |
