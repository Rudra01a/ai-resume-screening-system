from pathlib import Path
import shutil

import streamlit as st

from src.pipeline.pipeline import ResumeScreeningPipeline

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide",
)

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:
    st.title("📄 Resume Screening")

    st.markdown("### 👨‍💻 Developer")
    st.write("Rudra Pratap Singh")

    st.markdown("### ⚙️ Tech Stack")
    st.write(
        """
- Python
- Streamlit
- NLP
- TF-IDF
- Pandas
"""
    )

    st.markdown("### 📌 Instructions")
    st.write(
        """
1. Upload one or more resume PDFs.
2. Paste the job description.
3. Click **Rank Candidates**.
4. View rankings and download reports.
"""
    )

# ---------------------------
# Main UI
# ---------------------------
st.title("📄 AI Resume Screening System")

st.caption(
    "Upload resumes, paste a job description, and let AI rank the best candidates."
)

st.divider()

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True,
)

job_description = st.text_area(
    "Job Description",
    placeholder="Paste the job description here...",
    height=250,
)

# ---------------------------
# Run Pipeline
# ---------------------------
if st.button("🚀 Rank Candidates", use_container_width=True):

    if not uploaded_files:
        st.error("Please upload at least one resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:

        upload_dir = Path("temp_uploads")

        # Remove previous uploads
        if upload_dir.exists():
            shutil.rmtree(upload_dir)

        upload_dir.mkdir(parents=True, exist_ok=True)

        # Save uploaded resumes
        for uploaded_file in uploaded_files:
            with open(upload_dir / uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())

        with st.spinner("Ranking candidates..."):

            pipeline = ResumeScreeningPipeline(
                resumes_dir=upload_dir,
                job_description=job_description,
            )

            ranked_candidates = pipeline.run()

        # ---------------------------
        # Success Message
        # ---------------------------
        st.success("✅ Ranking completed successfully!")

        # ---------------------------
        # Metrics
        # ---------------------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Resumes", len(ranked_candidates))

        with col2:
            st.metric(
                "Top Score",
                f"{ranked_candidates.iloc[0]['final_score']:.3f}",
            )

        with col3:
            st.metric(
                "Top Candidate",
                ranked_candidates.iloc[0]["candidate_id"].replace("_", " "),
            )

        # ---------------------------
        # Best Candidate
        # ---------------------------
        st.subheader("🏆 Best Match")

        top = ranked_candidates.iloc[0]

        st.info(
            f"""
### {top['candidate_id'].replace('_', ' ')}

**Final Score:** {top['final_score']:.3f}

**TF-IDF Similarity:** {top['tfidf_similarity']:.3f}

**Skill Match:** {top['skill_match']:.2%}
"""
        )

        # ---------------------------
        # Rankings Table
        # ---------------------------
        st.subheader("🏆 Candidate Rankings")

        st.dataframe(
            ranked_candidates[
                [
                    "rank",
                    "candidate_id",
                    "final_score",
                    "tfidf_similarity",
                    "skill_match",
                ]
            ].style.format(
                {
                    "final_score": "{:.3f}",
                    "tfidf_similarity": "{:.3f}",
                    "skill_match": "{:.2%}",
                }
            ).highlight_max(
                subset=["final_score"]
            ),
            use_container_width=True,
        )

        # ---------------------------
        # Score Chart
        # ---------------------------
        st.subheader("📊 Candidate Score Distribution")

        chart = ranked_candidates.set_index("candidate_id")["final_score"]

        st.bar_chart(chart)

        # ---------------------------
        # Download Reports
        # ---------------------------
        st.subheader("📥 Download Reports")

        csv_path = Path("outputs") / "ranked_candidates.csv"
        pdf_path = Path("outputs") / "ranked_candidates.pdf"

        col1, col2 = st.columns([1, 1])

        with col1:
            if csv_path.exists():
                with open(csv_path, "rb") as f:
                    st.download_button(
                        label="⬇ Download CSV Report",
                        data=f,
                        file_name="ranked_candidates.csv",
                        mime="text/csv",
                        use_container_width=True,
                    )

        with col2:
            if pdf_path.exists():
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="⬇ Download PDF Report",
                        data=f,
                        file_name="ranked_candidates.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                    )