"""
Streamlit page: download generated reports.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import streamlit as st

st.title("Reports")

report_path = Path("outputs/ranked_candidates/ranked_candidates.csv")

if report_path.exists():
    with open(report_path, "rb") as f:
        st.download_button(
            "Download Ranked Candidates (CSV)",
            data=f,
            file_name="ranked_candidates.csv",
            mime="text/csv",
        )
else:
    st.info("No report generated yet — run the pipeline from the Ranking Dashboard page first.")
