"""
End-to-end pipeline orchestrator.

WHY THIS FILE EXISTS:
src/ modules are deliberately small and single-purpose - none of them
know about each other. Something has to call them in the right order and
wire outputs to inputs. This script is that "something", and it's also
what frontend/app.py calls into so the dashboard and a plain CLI run
share the exact same pipeline logic.

Usage:
    python scripts/run_pipeline.py
"""
import sys
from pathlib import Path

# Allow running as `python scripts/run_pipeline.py` from repo root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.parsing.text_extractor import extract_text
from src.preprocessing.cleaner import clean_text
from src.extraction.skill_extractor import extract_skills
from src.features.tfidf_features import TfidfFeatureBuilder
from src.similarity.cosine_similarity import compute_similarity
from src.similarity.scorer import compute_weighted_score
from src.features.feature_builder import build_feature_table
from src.ranking.weighting import get_ranking_weights
from src.ranking.ranker import rank_candidates
from src.reporting.report_generator import generate_csv_report
from src.utils.file_utils import list_resume_files, load_yaml
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run(config_path: str = "config/config.yaml"):
    config = load_yaml(config_path)

    resume_dir = Path(config["paths"]["raw_resumes"])
    jd_dir = Path(config["paths"]["raw_job_descriptions"])

    resume_files = list_resume_files(resume_dir)
    jd_files = list_resume_files(jd_dir)

    if not resume_files or not jd_files:
        logger.warning(
            "No resumes/job descriptions found. Add files to %s and %s first.",
            resume_dir, jd_dir,
        )
        return

    jd_text = clean_text(extract_text(jd_files[0]))

    candidate_ids, resume_texts, skill_scores = [], [], []
    jd_skills = set(extract_skills(jd_text))

    for resume_path in resume_files:
        text = clean_text(extract_text(resume_path))
        resume_texts.append(text)
        candidate_ids.append(resume_path.stem)

        candidate_skills = set(extract_skills(text))
        overlap = len(candidate_skills & jd_skills) / max(len(jd_skills), 1)
        skill_scores.append(overlap)

    tfidf_builder = TfidfFeatureBuilder(**config["features"]["tfidf"])
    resume_matrix = tfidf_builder.fit_transform(resume_texts + [jd_text])
    jd_vector = resume_matrix[-1]
    resume_matrix = resume_matrix[:-1]

    similarity_scores = compute_similarity(resume_matrix, jd_vector)

    weights = get_ranking_weights(config_path)
    final_scores = [
        compute_weighted_score(sim, skill, weights=weights)
        for sim, skill in zip(similarity_scores, skill_scores)
    ]

    feature_table = build_feature_table(candidate_ids, similarity_scores, skill_scores)
    ranked = rank_candidates(feature_table, final_scores, top_k=config["ranking"]["top_k"])

    output_path = Path(config["paths"]["ranked_output"]) / "ranked_candidates.csv"
    generate_csv_report(ranked, output_path)
    logger.info("Ranking complete. Results written to %s", output_path)

    return ranked


if __name__ == "__main__":
    run()
