"""
End-to-end Resume Screening Pipeline.
"""

from pathlib import Path

from src.parsing.pdf_parser import extract_text_from_pdf
from src.preprocessing.cleaner import clean_text
from src.preprocessing.normalizer import lemmatize
from src.extraction.skill_extractor import extract_skills


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

    def load_resumes(self):
        """
        Read every PDF resume from the resumes directory.
        """
        resumes = []

        pdf_files = sorted(self.resumes_dir.glob("*.pdf"))

        for pdf in pdf_files:
            print(f"Reading {pdf.name}")

            text = extract_text_from_pdf(pdf)

            resumes.append(
                {
                    "candidate_id": pdf.stem,
                    "filename": pdf.name,
                    "text": text,
                }
            )

        print(f"Loaded {len(resumes)} resumes.")

        return resumes

    def preprocess_resumes(self, resumes):
        """
        Clean and normalize the extracted resume text.
        """
        for resume in resumes:
            cleaned = clean_text(resume["text"])
            normalized = lemmatize(cleaned)

            resume["clean_text"] = normalized

        print(f"Preprocessed {len(resumes)} resumes.")

        return resumes

    def extract_resume_skills(self, resumes):
        """
        Extract technical skills from every resume.
        """
        for resume in resumes:
            skills = extract_skills(resume["clean_text"])

            resume["skills"] = skills

            print(
                f"{resume['candidate_id']} -> "
                f"{len(skills)} skills found"
            )

        print(f"Extracted skills from {len(resumes)} resumes.")

        return resumes

    def run(self):
        print("=" * 60)
        print("AI Resume Screening Pipeline")
        print("=" * 60)

        # Step 1
        resumes = self.load_resumes()

        # Step 2
        resumes = self.preprocess_resumes(resumes)

        # Step 3
        resumes = self.extract_resume_skills(resumes)

        print("\nPipeline started successfully.")