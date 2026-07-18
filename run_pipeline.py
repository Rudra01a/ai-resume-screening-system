from src.preprocessing.cleaner import clean_text
from src.preprocessing.normalizer import lemmatize
from src.pipeline.pipeline import ResumeScreeningPipeline

pipeline = ResumeScreeningPipeline(
    resumes_dir="data/raw/resumes",
    job_description="Python Machine Learning Engineer"
)

pipeline.run()