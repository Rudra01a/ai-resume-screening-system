"""
Unified entrypoint for parsing/. Dispatches to the right parser based on
file extension so the rest of the pipeline never needs to know whether a
resume was a PDF or DOCX.
"""
from pathlib import Path

from src.parsing.pdf_parser import extract_text_from_pdf
from src.parsing.docx_parser import extract_text_from_docx

SUPPORTED_EXTENSIONS = {".pdf", ".docx"}


def extract_text(file_path: str | Path) -> str:
    """
    Extract raw text from a resume file, regardless of format.

    Args:
        file_path: path to a .pdf or .docx resume.

    Raises:
        ValueError: if the file extension is not supported.

    Returns:
        Raw extracted text.
    """
    file_path = Path(file_path)
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        return extract_text_from_pdf(file_path)
    elif suffix == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(
            f"Unsupported file type '{suffix}'. "
            f"Supported: {SUPPORTED_EXTENSIONS}"
        )
