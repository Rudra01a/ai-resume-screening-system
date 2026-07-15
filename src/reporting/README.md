# src/reporting/

**Purpose:** Turn the final ranked DataFrame into shareable output files.

| File | Responsibility |
|---|---|
| `report_generator.py` | CSV export + fpdf2-based PDF report generation |
| `templates/` | (future) Jinja2/HTML templates for richer report layouts |

Outputs are written to `outputs/reports/` (git-ignored, regenerable).
