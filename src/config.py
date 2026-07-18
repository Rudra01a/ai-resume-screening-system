"""
Project Configuration
"""

from pathlib import Path

# ==========================
# Directories
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

RESUMES_DIR = BASE_DIR / "data" / "resumes"

OUTPUT_DIR = BASE_DIR / "outputs"

# ==========================
# Scoring Weights
# ==========================

TFIDF_WEIGHT = 0.60

SKILL_WEIGHT = 0.40

# ==========================
# Job Information
# ==========================

JOB_TITLE = "Data Scientist"

# ==========================
# Logging
# ==========================

LOG_LEVEL = "INFO"