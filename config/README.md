# config/

Holds every tunable setting for the pipeline: file paths, preprocessing
switches, TF-IDF hyperparameters, ranking weights, and logging setup.

**Why a dedicated folder:** hardcoding thresholds and weights inside
Python modules makes them invisible to non-engineers (recruiters, PMs)
and forces a code change + redeploy for every tuning tweak. Centralizing
them here means:

- `config.yaml` — master pipeline configuration
- `skills_taxonomy.yaml` — editable skill dictionary (domain experts can extend this without touching code)
- `logging.yaml` — standard logging setup shared by every module

Load these with `src/utils/file_utils.py::load_yaml()`.
