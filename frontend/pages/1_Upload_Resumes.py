"""
Streamlit page: upload resume files into data/raw/resumes/.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import streamlit as st

st.title("Upload Resumes")

uploaded_files = st.file_uploader(
    "Upload candidate resumes (PDF or DOCX)",
    type=["pdf", "docx"],
    accept_multiple_files=True,
)

if uploaded_files:
    target_dir = Path("data/raw/resumes")
    target_dir.mkdir(parents=True, exist_ok=True)

    for uploaded_file in uploaded_files:
        out_path = target_dir / uploaded_file.name
        out_path.write_bytes(uploaded_file.getbuffer())

    st.success(f"Saved {len(uploaded_files)} resume(s) to {target_dir}/")
