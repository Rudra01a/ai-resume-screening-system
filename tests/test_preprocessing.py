"""
Unit tests for src/preprocessing/.
"""


def test_clean_text_lowercases_and_strips_punctuation():
    from src.preprocessing.cleaner import clean_text

    raw = "Python, Java & C++!!  \n\n Skills:"
    cleaned = clean_text(raw)

    assert cleaned == cleaned.lower()
    assert "!" not in cleaned
    assert "  " not in cleaned  # whitespace collapsed


def test_tokenize_removes_stopwords():
    from src.preprocessing.tokenizer import tokenize

    tokens = tokenize("this is a test of the tokenizer", remove_stopwords=True)
    assert "is" not in tokens
    assert "test" in tokens
