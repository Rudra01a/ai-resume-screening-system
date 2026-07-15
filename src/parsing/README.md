# src/parsing/

**Purpose:** Convert raw resume files (PDF/DOCX) into plain text strings.
This is the only layer allowed to touch binary file formats.

| File | Responsibility |
|---|---|
| `pdf_parser.py` | PyPDF2-based text extraction from `.pdf` |
| `docx_parser.py` | python-docx-based text extraction from `.docx` |
| `text_extractor.py` | Public dispatcher — the rest of the app should import *this*, not the individual parsers |

**Extending later:** add an `image_ocr_parser.py` here (e.g. Tesseract)
for scanned resumes without changing anything downstream — `text_extractor.py`
is the single seam that needs updating.
