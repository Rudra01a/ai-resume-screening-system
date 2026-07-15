"""
PLACEHOLDER — dense embedding-based features (roadmap: LLM integration).

STATUS: not yet implemented. TF-IDF (tfidf_features.py) captures lexical
overlap only; it cannot tell that "built ML models" and "developed
machine learning systems" mean the same thing. This module is where
sentence-transformer or LLM-based embeddings would plug in, exposing the
same fit_transform()/transform() interface as TfidfFeatureBuilder so
similarity/cosine_similarity.py doesn't need to change.

Planned implementation:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(documents)
"""

# TODO(roadmap): implement EmbeddingFeatureBuilder with the same
# interface as TfidfFeatureBuilder (fit_transform / transform / save / load)
