"""
Unit tests for src/parsing/. Add sample fixture files under
tests/fixtures/ (create as needed) rather than relying on data/raw/.
"""
import pytest


def test_extract_text_unsupported_extension(tmp_path):
    from src.parsing.text_extractor import extract_text

    bad_file = tmp_path / "resume.txt"
    bad_file.write_text("hello")

    with pytest.raises(ValueError):
        extract_text(bad_file)


# TODO: add test_extract_text_from_pdf using a small fixture PDF
# TODO: add test_extract_text_from_docx using a small fixture DOCX
