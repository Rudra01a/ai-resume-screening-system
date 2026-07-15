"""
similarity/  — Stage 5 of the pipeline.

WHY THIS FOLDER EXISTS:
Once resumes and the job description are numeric vectors (features/), we
need a single number per candidate expressing "how close is this resume
to this job description". That comparison logic lives here, isolated
from both feature extraction (features/) and score aggregation (ranking/).
"""
