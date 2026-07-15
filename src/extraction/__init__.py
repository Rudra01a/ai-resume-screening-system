"""
extraction/  — Stage 3 of the pipeline.

WHY THIS FOLDER EXISTS:
Clean text is still unstructured. To rank candidates meaningfully we need
structured signal pulled OUT of that text: which skills appear, what
entities (companies, degrees, dates) are mentioned, and which section of
the resume a piece of text belongs to (Experience vs Education vs Skills).
This is the layer where "text" becomes "facts about a candidate".
"""
