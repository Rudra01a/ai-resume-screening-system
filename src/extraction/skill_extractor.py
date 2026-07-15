"""
Match resume/JD text against the skills taxonomy (config/skills_taxonomy.yaml)
using spaCy's PhraseMatcher for fast, multi-word-phrase matching.
"""
import spacy
from spacy.matcher import PhraseMatcher

from src.utils.file_utils import load_yaml

_NLP = None
_MATCHER = None
_ALL_SKILLS: list[str] = []


def _build_matcher(taxonomy_path: str = "config/skills_taxonomy.yaml", model_name: str = "en_core_web_sm"):
    global _NLP, _MATCHER, _ALL_SKILLS
    if _MATCHER is not None:
        return _NLP, _MATCHER

    _NLP = spacy.load(model_name, disable=["ner", "parser"])
    taxonomy = load_yaml(taxonomy_path)

    _ALL_SKILLS = [skill for group in taxonomy.values() for skill in group]
    _MATCHER = PhraseMatcher(_NLP.vocab, attr="LOWER")
    patterns = [_NLP.make_doc(skill) for skill in _ALL_SKILLS]
    _MATCHER.add("SKILLS", patterns)

    return _NLP, _MATCHER


def extract_skills(text: str, taxonomy_path: str = "config/skills_taxonomy.yaml") -> list[str]:
    """
    Return the deduplicated list of known skills found in `text`.

    Args:
        text: cleaned resume or job-description text.
        taxonomy_path: path to the YAML skills taxonomy.

    Returns:
        Sorted list of matched skill strings.
    """
    nlp, matcher = _build_matcher(taxonomy_path)
    doc = nlp(text)
    matches = matcher(doc)
    found = {doc[start:end].text.lower() for _, start, end in matches}
    return sorted(found)
