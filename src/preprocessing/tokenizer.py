"""
Tokenization + stopword removal using NLTK.
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required corpora on first run (no-op if already present).
for resource in ("punkt", "punkt_tab", "stopwords"):
    try:
        nltk.data.find(f"tokenizers/{resource}")
    except LookupError:
        nltk.download(resource, quiet=True)

_STOPWORDS = set(stopwords.words("english"))


def tokenize(text: str, remove_stopwords: bool = True) -> list[str]:
    """
    Split cleaned text into tokens, optionally removing English stopwords.

    Args:
        text: cleaned text (output of cleaner.clean_text).
        remove_stopwords: drop common stopwords if True.

    Returns:
        List of tokens.
    """
    tokens = word_tokenize(text)
    if remove_stopwords:
        tokens = [t for t in tokens if t not in _STOPWORDS]
    return tokens
