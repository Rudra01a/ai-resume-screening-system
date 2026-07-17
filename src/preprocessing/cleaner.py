"""
Basic text cleaning: whitespace, punctuation, special characters.
"""
import re


def clean_text(text: str, remove_punctuation: bool = True, lowercase: bool = True) -> str:
    """
    Normalize whitespace and optionally strip punctuation/casing.

    Args:
        text: raw text (typically straight from parsing/text_extractor.py).
        remove_punctuation: strip non-alphanumeric characters if True.
        lowercase: lowercase everything if True.

    Returns:
        Cleaned text string.
    """
    text = re.sub(r"\s+", " ", text)          # collapse whitespace/newlines
    text = re.sub(r"[•●▪○]", " ", text)        # strip common bullet glyphs

    if remove_punctuation:
        text = re.sub(r"[^a-zA-Z0-9@.\s]", " ", text)  # keep @ and . for emails
    if lowercase:
        text = text.lower()

    # Collapse whitespace again after punctuation removal
        text = re.sub(r"\s+", " ", text)

        return text.strip()