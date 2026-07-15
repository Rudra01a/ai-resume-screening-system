# src/utils/

**Purpose:** Shared helpers with no business logic of their own —
config loading, logging setup, project-wide constants.

| File | Responsibility |
|---|---|
| `file_utils.py` | YAML loading, resume file listing |
| `logger.py` | Central logging setup (reads `config/logging.yaml`) |
| `constants.py` | Fixed values shared across modules |

**Rule of thumb:** if a helper function is used by 2+ other `src/`
packages and has no domain-specific logic, it belongs here.
