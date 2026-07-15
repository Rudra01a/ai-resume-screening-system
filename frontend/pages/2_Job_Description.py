"""
Streamlit page: upload/paste the job description used as the ranking target.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import streamlit as st

st.title("Job Description")

jd_text = st.text_area("Paste the job description here", height=300)

if st.button("Save Job Description"):
    if jd_text.strip():
        target_dir = Path("data/raw/job_descriptions")
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "job_description.txt").write_text(jd_text)
        st.success("Job description saved.")
    else:
        st.warning("Please paste a job description first.")
