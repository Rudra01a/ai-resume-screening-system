"""
preprocessing/  — Stage 2 of the pipeline.

WHY THIS FOLDER EXISTS:
Raw extracted text is messy (extra whitespace, bullet characters, headers/
footers, mixed casing). Every downstream stage (skill extraction, TF-IDF)
performs better on normalized text. This package's job:
    raw text in  ->  clean, tokenized, normalized text out
"""
