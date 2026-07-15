"""
Main Streamlit entrypoint.

WHY THIS FILE EXISTS:
Streamlit's multipage app convention auto-discovers files under pages/
and lists them in a sidebar. This file (app.py) is the "Home" page and
the file you run with `streamlit run frontend/app.py`.

This file (and everything in frontend/) ONLY handles presentation - it
calls into scripts/run_pipeline.py and src/ for all actual logic, per
the clean-architecture dependency rule (see docs/architecture.md).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st

st.set_page_config(
    page_title="Resume Screening & Ranking",
    page_icon="\U0001F4C4",
    layout="wide",
)

st.title("AI-Powered Resume Screening & Candidate Ranking")

st.markdown(
    """
    Welcome! Use the sidebar to navigate:

    1. **Upload Resumes** — add candidate resumes and a job description
    2. **Job Description** — review/edit the parsed job description
    3. **Ranking Dashboard** — view scored, ranked candidates
    4. **Reports** — download PDF/CSV reports

    This dashboard is a thin presentation layer over the pipeline in
    `src/` and `scripts/run_pipeline.py` — all NLP/ML logic lives there
    and can be run headlessly (`python scripts/run_pipeline.py`) without
    this UI at all.
    """
)
