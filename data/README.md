# data/

The project's data lake, split by processing stage. This separation
(raw → interim → processed) is a standard data-engineering pattern that
guarantees you can always regenerate downstream data without touching
the original source files.

| Folder | Contents | Mutable? |
|---|---|---|
| `raw/resumes/` | Original uploaded resumes (PDF/DOCX), untouched | Never edit by hand |
| `raw/job_descriptions/` | Original job description text/files | Never edit by hand |
| `interim/` | Intermediate artifacts: extracted raw text, partially cleaned text | Regenerable |
| `processed/` | Final cleaned/tokenized text + feature matrices ready for modeling | Regenerable |
| `external/` | Third-party reference data (e.g. an external skills database, market salary data) | Rarely changes |

**Why this matters for this project specifically:** resumes contain PII
(names, emails, phone numbers). Keeping raw candidate data physically
isolated in `raw/` and git-ignored (see root `.gitignore`) makes it easy
to enforce "never commit real candidate data" as a hard rule, while still
versioning the *pipeline code* that processes it.
