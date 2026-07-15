# src/preprocessing/

**Purpose:** Turn raw parsed text into clean, tokenized, normalized text
suitable for feature extraction.

| File | Responsibility |
|---|---|
| `cleaner.py` | Whitespace/punctuation/casing normalization |
| `tokenizer.py` | NLTK word tokenization + stopword removal |
| `normalizer.py` | spaCy lemmatization |

**Pipeline order:** `cleaner.clean_text()` → `tokenizer.tokenize()` and/or
`normalizer.lemmatize()`, depending on whether downstream code wants a
token list (skill matching) or a normalized string (TF-IDF vectorizer).
