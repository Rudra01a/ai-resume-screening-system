# models/

Serialized, regenerable artifacts — **never source code, never manually
edited.** Everything here is git-ignored except `.gitkeep` placeholders;
re-run `scripts/run_pipeline.py` to regenerate.

| Folder | Contents |
|---|---|
| `trained/` | Any trained model objects (e.g. a future learned ranker from `src/feedback/`) |
| `vectorizers/` | Pickled, fitted `TfidfVectorizer` objects from `src/features/tfidf_features.py` |

**Why version-controlled placeholders but not contents:** trained
artifacts can be large and are fully reproducible from `data/` + `src/`,
so committing them would bloat the repo without adding information.
