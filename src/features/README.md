# src/features/

**Purpose:** Convert normalized text into numeric feature representations
that similarity/ranking algorithms can consume.

| File | Responsibility |
|---|---|
| `tfidf_features.py` | scikit-learn TF-IDF vectorization (current default) |
| `feature_builder.py` | Combines multiple signals into one per-candidate feature table |
| `embeddings.py` | **Roadmap placeholder** for LLM/sentence-embedding features |

**Design note:** `tfidf_features.py` and `embeddings.py` are built to
expose the same interface (`fit_transform`/`transform`/`save`/`load`) so
`similarity/` can be pointed at either without modification.
