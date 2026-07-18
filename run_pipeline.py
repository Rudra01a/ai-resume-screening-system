from pathlib import Path

from src.pipeline.pipeline import ResumeScreeningPipeline


job_description_path = Path("data/raw/job_descriptions/job_description.txt")

job_description = job_description_path.read_text(encoding="utf-8")


pipeline = ResumeScreeningPipeline(
    resumes_dir="data/raw/resumes",
    job_description=job_description,
)

pipeline.run()