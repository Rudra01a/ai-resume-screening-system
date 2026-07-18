from pathlib import Path

import pandas as pd

from src.reporting.report_generator import (
    generate_csv_report,
    generate_pdf_report,
)


def test_generate_reports(tmp_path):
    ranked_df = pd.DataFrame(
        {
            "rank": [1, 2],
            "candidate_id": ["c1", "c2"],
            "final_score": [0.95, 0.87],
        }
    )

    csv_path = tmp_path / "report.csv"
    pdf_path = tmp_path / "report.pdf"

    generate_csv_report(ranked_df, csv_path)
    generate_pdf_report(ranked_df, pdf_path)

    assert csv_path.exists()
    assert pdf_path.exists()