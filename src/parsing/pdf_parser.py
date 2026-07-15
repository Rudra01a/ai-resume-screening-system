"""
Extract raw text from PDF resumes using PyPDF2.

Kept deliberately dumb: no cleaning/formatting logic here, just
byte-stream -> text. See preprocessing/ for cleaning.
"""
from pathlib import Path
from PyPDF2 import PdfReader


def extract_text_from_pdf(file_path: str | Path) -> str:
    """
    Read a PDF file and return its concatenated text content.

    Args:
        file_path: path to a .pdf resume file.

    Returns:
        Extracted text (may be empty string if the PDF is a scanned
        image with no embedded text layer — OCR is out of scope here).
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    reader = PdfReader(str(file_path))
    pages_text = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages_text.append(text)

    return "\n".join(pages_text)


if __name__ == "__main__":
    # quick manual smoke test:
    #   python -m src.parsing.pdf_parser path/to/resume.pdf
    import sys
    if len(sys.argv) > 1:
        print(extract_text_from_pdf(sys.argv[1])[:500])
