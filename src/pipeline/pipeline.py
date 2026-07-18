"""
End-to-end Resume Screening Pipeline.
"""

from pathlib import Path

from src.similarity.cosine_similarity import compute_similarity
from src.similarity.skill_match import compute_skill_match
from src.similarity.scorer import compute_weighted_score
from src.parsing.pdf_parser import extract_text_from_pdf
from src.preprocessing.cleaner import clean_text
from src.preprocessing.normalizer import lemmatize
from src.extraction.skill_extractor import extract_skills
from src.features.tfidf_features import TfidfFeatureBuilder
from src.features.feature_builder import build_feature_table
from src.ranking.ranker import rank_candidates
from src.reporting.report_generator import (
    generate_csv_report,
    generate_pdf_report,
)
from src.utils.logger import get_logger


class ResumeScreeningPipeline:

    def __init__(
        self,
        resumes_dir: str | Path,
        job_description: str,
        output_dir: str | Path = "outputs",
    ):
        self.resumes_dir = Path(resumes_dir)
        self.job_description = job_description
        self.output_dir = Path(output_dir)

        self.logger = get_logger()

    def load_resumes(self):
        self.logger.info("Loading resumes...")

        try:
            resumes = []

            pdf_files = sorted(self.resumes_dir.glob("*.pdf"))

            if not pdf_files:
                raise FileNotFoundError(
                    f"No PDF files found in {self.resumes_dir}"
                )

            for pdf in pdf_files:
                print(f"Reading {pdf.name}")
                self.logger.info(f"Reading {pdf.name}")

                text = extract_text_from_pdf(pdf)

                resumes.append(
                    {
                        "candidate_id": pdf.stem,
                        "filename": pdf.name,
                        "text": text,
                    }
                )

            print(f"Loaded {len(resumes)} resumes.")
            self.logger.info(f"Loaded {len(resumes)} resumes.")

            return resumes

        except Exception:
            self.logger.exception("Error while loading resumes.")
            raise

    def preprocess_resumes(self, resumes):
        self.logger.info("Preprocessing resumes...")

        for resume in resumes:
            cleaned = clean_text(resume["text"])
            normalized = lemmatize(cleaned)

            resume["clean_text"] = normalized

        print(f"Preprocessed {len(resumes)} resumes.")
        self.logger.info(f"Preprocessed {len(resumes)} resumes.")

        return resumes

    def extract_resume_skills(self, resumes):
        self.logger.info("Extracting skills from resumes...")

        for resume in resumes:
            skills = extract_skills(resume["clean_text"])

            resume["skills"] = skills

            print(
                f"{resume['candidate_id']} -> "
                f"{len(skills)} skills found"
        )

        self.logger.info(
            f"{resume['candidate_id']} -> {len(skills)} skills extracted"
        )

        print(f"Extracted skills from {len(resumes)} resumes.")
        self.logger.info("Resume skill extraction completed.")

        return resumes
    

    def extract_job_skills(self):
        self.logger.info("Extracting job description skills...")

        job_skills = extract_skills(self.job_description)

        print(f"Job Description -> {len(job_skills)} skills found")

        self.logger.info(
            f"Extracted {len(job_skills)} skills from the job description."
    )

        return job_skills



    def build_tfidf_features(self, resumes):
        documents = [resume["clean_text"] for resume in resumes]
        documents.append(self.job_description)

        builder = TfidfFeatureBuilder()

        self.logger.info("Building TF-IDF feature matrix...")

        tfidf_matrix = builder.fit_transform(documents)

        print("Built TF-IDF feature matrix.")

        self.logger.info("TF-IDF feature matrix built successfully.")

        return builder, tfidf_matrix



    def compute_tfidf_similarity(self, builder, tfidf_matrix, resumes):
        resume_matrix = tfidf_matrix[:-1]
        job_vector = builder.transform([self.job_description])

        similarity_scores = compute_similarity(
            resume_matrix,
            job_vector,
        )

        print("\nCosine Similarity Scores")
        print("-" * 40)

        for resume, score in zip(resumes, similarity_scores):
            print(f"{resume['candidate_id']}: {score:.4f}")

        print("-" * 40)

        return similarity_scores

    def compute_skill_match_scores(self, resumes, job_skills):
        skill_scores = []

        print("\nSkill Match Scores")
        print("-" * 40)

        for resume in resumes:
            score = compute_skill_match(
                resume["skills"],
                job_skills,
            )

            skill_scores.append(score)

            print(f"{resume['candidate_id']}: {score:.2f}%")

        print("-" * 40)

        return skill_scores

    def compute_final_scores(
        self,
        resumes,
        similarity_scores,
        skill_scores,
    ):
        final_scores = []

        print("\nFinal Weighted Scores")
        print("-" * 40)

        for resume, similarity, skill in zip(
            resumes,
            similarity_scores,
            skill_scores,
        ):
            score = compute_weighted_score(
                tfidf_similarity=similarity,
                skill_match=skill,
            )

            final_scores.append(score)

            print(f"{resume['candidate_id']}: {score:.4f}")

        print("-" * 40)

        return final_scores

    def rank_resumes(
        self,
        resumes,
        similarity_scores,
        skill_scores,
        final_scores,
    ):
        """
        Build feature table and rank candidates.
        """

        candidate_ids = [
            resume["candidate_id"]
            for resume in resumes
        ]

        feature_table = build_feature_table(
            candidate_ids=candidate_ids,
            tfidf_scores=similarity_scores,
            skill_match_scores=skill_scores,
        )

        ranked = rank_candidates(
            feature_table=feature_table,
            scores=final_scores,
        )

        print("\nFinal Candidate Ranking")
        print("-" * 80)

        print(
            ranked[
                [
                    "rank",
                    "candidate_id",
                    "tfidf_similarity",
                    "skill_match",
                    "final_score",
                ]
            ].to_string(index=False)
        )

        print("-" * 80)

        return ranked

    def generate_reports(self, ranked_candidates):
        """
        Generate CSV and PDF reports.
        """

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        csv_path = self.output_dir / "ranked_candidates.csv"
        pdf_path = self.output_dir / "ranked_candidates.pdf"

        generate_csv_report(
            ranked_candidates,
            csv_path,
        )

        generate_pdf_report(
            ranked_candidates,
            pdf_path,
            job_title="Data Scientist",
        )

        print("\nReports Generated")
        print("-" * 40)
        print(f"CSV Report : {csv_path}")
        print(f"PDF Report : {pdf_path}")
        print("-" * 40)

    def run(self):
        print("=" * 60)
        print("AI Resume Screening Pipeline")
        print("=" * 60)

        self.logger.info("Pipeline started.")

        # Step 1: Load resumes
        resumes = self.load_resumes()

        # Step 2: Preprocess resumes
        resumes = self.preprocess_resumes(resumes)

        # Step 3: Extract skills
        resumes = self.extract_resume_skills(resumes)

        # Step 4: Extract job description skills
        job_skills = self.extract_job_skills()

        # Step 5: Build TF-IDF features
        builder, tfidf_matrix = self.build_tfidf_features(resumes)

        # Step 6: Compute cosine similarity
        similarity_scores = self.compute_tfidf_similarity(
            builder,
            tfidf_matrix,
            resumes,
        )

        # Step 7: Compute skill match
        skill_scores = self.compute_skill_match_scores(
            resumes,
            job_skills,
        )

        # Step 8: Compute weighted scores
        final_scores = self.compute_final_scores(
            resumes,
            similarity_scores,
            skill_scores,
        )

        # Step 9: Rank candidates
        ranked_candidates = self.rank_resumes(
            resumes,
            similarity_scores,
            skill_scores,
            final_scores,
        )

        # Step 10: Generate reports
        self.generate_reports(
            ranked_candidates,
        )

        print("\nPipeline completed successfully.")

        self.logger.info("Pipeline completed successfully.")

        return ranked_candidates