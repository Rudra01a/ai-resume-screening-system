"""
Named Entity Recognition (NER) over resume text using spaCy's built-in NER.

STATUS: functional baseline using spaCy's generic NER model. This is the
designated extension point for the "Named Entity Recognition" roadmap
item — e.g. swapping in a resume-specific fine-tuned NER model
(companies, degrees, universities, job titles) without touching any
other module, since callers only depend on `extract_entities()`.
"""
import spacy

_NLP = None


def _get_nlp(model_name: str = "en_core_web_sm"):
    global _NLP
    if _NLP is None:
        _NLP = spacy.load(model_name)
    return _NLP


def extract_entities(text: str, model_name: str = "en_core_web_sm") -> dict[str, list[str]]:
    """
    Extract named entities grouped by label (ORG, GPE, DATE, PERSON, etc.).

    Args:
        text: raw or lightly cleaned resume text (avoid over-cleaning,
              since NER benefits from original casing/punctuation).

    Returns:
        Dict mapping entity label -> list of entity strings, e.g.
        {"ORG": ["Google", "IIT BHU"], "DATE": ["2023", "2024"]}
    """
    nlp = _get_nlp(model_name)
    doc = nlp(text)

    entities: dict[str, list[str]] = {}
    for ent in doc.ents:
        entities.setdefault(ent.label_, []).append(ent.text)

    return entities
