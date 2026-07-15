"""
Lemmatization using spaCy. Kept separate from tokenizer.py because
lemmatization needs a loaded spaCy model (heavier dependency, loaded once
and reused) whereas tokenization only needs NLTK.
"""
import spacy

_NLP = None


def _get_nlp(model_name: str = "en_core_web_sm"):
    """Lazily load the spaCy model once per process."""
    global _NLP
    if _NLP is None:
        _NLP = spacy.load(model_name, disable=["ner", "parser"])
    return _NLP


def lemmatize(text: str, model_name: str = "en_core_web_sm") -> str:
    """
    Lemmatize text (e.g. "developing" -> "develop").

    Args:
        text: cleaned text.
        model_name: spaCy model to use.

    Returns:
        Space-joined lemmatized text.
    """
    nlp = _get_nlp(model_name)
    doc = nlp(text)
    return " ".join(token.lemma_ for token in doc if not token.is_space)
