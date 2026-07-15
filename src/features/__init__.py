"""
features/  — Stage 4 of the pipeline.

WHY THIS FOLDER EXISTS:
Machine learning/similarity math can't operate on strings directly - text
must become numeric vectors first. This package owns that conversion,
and is the designated seam for swapping TF-IDF for embeddings later
(see embeddings.py) without touching similarity/ or ranking/.
"""
