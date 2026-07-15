# src/extraction/

**Purpose:** Convert clean/raw text into structured facts about a
candidate: skills present, named entities, and resume sections.

| File | Responsibility |
|---|---|
| `skill_extractor.py` | Matches text against `config/skills_taxonomy.yaml` via spaCy PhraseMatcher |
| `entity_extractor.py` | spaCy NER — **extension point for the roadmap's NER item** |
| `section_segmenter.py` | Regex-based splitting into Education/Experience/Skills/etc. |

**Why separate from preprocessing/:** preprocessing only transforms text
(cleaning/tokenizing); extraction *interprets* it (what does this text
mean about the candidate). Keeping them separate means you can improve
skill-matching logic without touching cleaning logic, and vice versa.
