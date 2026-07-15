# notebooks/

Jupyter notebooks for **exploratory analysis only** — trying out a new
skill-matching regex, visualizing TF-IDF score distributions, debugging
why a particular resume parsed oddly.

**Hard rule:** nothing in here is imported by `src/`, `frontend/`, or
`scripts/`. If a notebook cell turns out to be genuinely useful pipeline
logic, promote it into the appropriate `src/` module — notebooks are a
scratchpad, not a deployment target.

Suggested naming convention: `01_eda_resume_lengths.ipynb`,
`02_tfidf_score_distribution.ipynb`, etc. (numbered = chronological).
