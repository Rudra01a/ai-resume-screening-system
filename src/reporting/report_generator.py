"""
Generate a PDF/CSV report from the final ranked candidate DataFrame.
"""
from pathlib import Path
import pandas as pd
from fpdf import FPDF


def generate_csv_report(ranked_df: pd.DataFrame, output_path: str | Path) -> Path:
    """Write the ranked candidate table to CSV."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ranked_df.to_csv(output_path, index=False)
    return output_path


def generate_pdf_report(ranked_df: pd.DataFrame, output_path: str | Path,
                         job_title: str = "Job Opening") -> Path:
    """
    Render a simple one-page-per-summary PDF listing ranked candidates.

    Args:
        ranked_df: output of ranking/ranker.py::rank_candidates().
        output_path: where to save the .pdf file.
        job_title: heading text for the report.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, f"Candidate Ranking Report - {job_title}", ln=True)
    pdf.set_font("Helvetica", "", 11)

    for _, row in ranked_df.iterrows():
        line = f"#{row['rank']}  {row['candidate_id']}  |  score: {row['final_score']:.3f}"
        pdf.cell(0, 8, line, ln=True)

    pdf.output(str(output_path))
    return output_path
