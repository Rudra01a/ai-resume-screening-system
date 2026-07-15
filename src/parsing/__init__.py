"""
parsing/  — Stage 1 of the pipeline.

WHY THIS FOLDER EXISTS:
Resumes arrive as PDF or DOCX binary files. Nothing downstream (cleaning,
tokenizing, feature extraction) can operate on a binary file — everything
needs plain text first. This package's only job is:
    binary file in  ->  raw text string out
It deliberately does NOT clean, tokenize, or interpret the text; that
belongs to preprocessing/ and extraction/, keeping each stage testable
in isolation.
"""
