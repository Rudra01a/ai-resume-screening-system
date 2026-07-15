# frontend/

Streamlit multipage dashboard — the **only** layer that knows about UI
concerns. Everything here calls into `scripts/run_pipeline.py` and `src/`
for actual logic (see `docs/architecture.md`'s dependency rule).

| Path | Purpose |
|---|---|
| `app.py` | Home page / entrypoint — run with `streamlit run frontend/app.py` |
| `pages/1_Upload_Resumes.py` | Upload candidate resumes |
| `pages/2_Job_Description.py` | Paste/save the target job description |
| `pages/3_Ranking_Dashboard.py` | Trigger the pipeline, view ranked results |
| `pages/4_Reports.py` | Download generated CSV/PDF reports |
| `components/` | Reusable widgets shared across multiple pages |
| `assets/` | CSS/static assets |

Streamlit auto-numbers sidebar pages by the `N_` filename prefix — keep
that convention when adding new pages.
