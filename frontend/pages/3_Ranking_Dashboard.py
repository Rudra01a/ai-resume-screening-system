"""
Streamlit page: run the pipeline and display the ranked candidate table.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import streamlit as st
from scripts.run_pipeline import run

st.title("Ranking Dashboard")

if st.button("Run Screening Pipeline"):
    with st.spinner("Parsing resumes, extracting skills, scoring candidates..."):
        ranked_df = run()

    if ranked_df is not None:
        st.session_state["ranked_df"] = ranked_df

if "ranked_df" in st.session_state:
    st.dataframe(st.session_state["ranked_df"], use_container_width=True)
else:
    st.info("Upload resumes + a job description, then click 'Run Screening Pipeline'.")
