"""
Generate professional PDF and CSV reports for ranked candidates.
"""

from pathlib import Path
from datetime import datetime

import pandas as pd
from fpdf import FPDF


def generate_csv_report(
    ranked_df: pd.DataFrame,
    output_path: str | Path,
) -> Path:
    """
    Generate a formatted CSV report.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    report = ranked_df.copy()

    report["tfidf_similarity"] = report["tfidf_similarity"].round(4)
    report["skill_match"] = (report["skill_match"] * 100).round(2)
    report["final_score"] = report["final_score"].round(4)

    report.rename(
        columns={
            "tfidf_similarity": "TF-IDF Similarity",
            "skill_match": "Skill Match (%)",
            "final_score": "Final Score",
        },
        inplace=True,
    )

    report.to_csv(output_path, index=False)

    return output_path


def generate_pdf_report(
    ranked_df: pd.DataFrame,
    output_path: str | Path,
    job_title: str = "Job Opening",
) -> Path:
    """
    Generate a professional PDF report.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # ---------- Title ----------

    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, "AI Resume Screening Report", new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.ln(4)

    # ---------- Information ----------

    pdf.set_font("Helvetica", "", 11)

    pdf.cell(0, 8, f"Job Title : {job_title}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(
        0,
        8,
        f"Generated : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.cell(
        0,
        8,
        f"Candidates Processed : {len(ranked_df)}",
        new_x="LMARGIN",
        new_y="NEXT",
    )

    pdf.ln(5)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Candidate Ranking", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 10)

    pdf.cell(15, 8, "Rank", border=1)
    pdf.cell(95, 8, "Candidate", border=1)
    pdf.cell(35, 8, "Score", border=1, align="C")
    pdf.ln()

    for _, row in ranked_df.iterrows():

        pdf.cell(15, 8, str(row["rank"]), border=1)

        pdf.cell(
            95,
            8,
            str(row["candidate_id"])[:38],
            border=1,
        )

        pdf.cell(
            35,
            8,
            f"{row['final_score']:.3f}",
            border=1,
            align="C",
        )

        pdf.ln()

    pdf.ln(10)

    # ---------- Top Candidate ----------

    top = ranked_df.iloc[0]

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Top Candidate", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 11)

    pdf.cell(
        0,
        8,
        f"Candidate : {top['candidate_id']}",
        new_x="LMARGIN",
        new_y="NEXT",
    )

    pdf.cell(
        0,
        8,
        f"Final Score : {top['final_score']:.3f}",
        new_x="LMARGIN",
        new_y="NEXT",
    )

    pdf.ln(8)

    pdf.set_font("Helvetica", "I", 9)

    pdf.cell(
        0,
        8,
        "Generated automatically by AI Resume Screening System",
        align="C",
    )

    pdf.output(str(output_path))

    return output_path