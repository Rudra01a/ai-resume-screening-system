"""
Extract raw text from DOCX resumes using python-docx.
"""
from pathlib import Path
from docx import Document


def extract_text_from_docx(file_path: str | Path) -> str:
    """
    Read a DOCX file and return its concatenated paragraph text.

    Args:
        file_path: path to a .docx resume file.

    Returns:
        Extracted text, paragraphs joined by newlines.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"DOCX not found: {file_path}")

    document = Document(str(file_path))
    paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)
