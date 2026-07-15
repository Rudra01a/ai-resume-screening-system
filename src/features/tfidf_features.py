"""
TF-IDF vectorization wrapper around scikit-learn's TfidfVectorizer.
"""
import pickle
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer


class TfidfFeatureBuilder:
    """
    Thin wrapper so the rest of the app depends on this class, not
    directly on sklearn - makes it easy to swap vectorizers later.
    """

    def __init__(self, max_features: int = 5000, ngram_range: tuple = (1, 2),
                 min_df: int = 1, max_df: float = 0.9):
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=ngram_range,
            min_df=min_df,
            max_df=max_df,
        )
        self._is_fitted = False

    def fit_transform(self, documents: list[str]):
        """Fit the vectorizer on a corpus (resumes + JD) and transform it."""
        matrix = self.vectorizer.fit_transform(documents)
        self._is_fitted = True
        return matrix

    def transform(self, documents: list[str]):
        """Transform new documents using an already-fitted vectorizer."""
        if not self._is_fitted:
            raise RuntimeError("Vectorizer must be fit before calling transform().")
        return self.vectorizer.transform(documents)

    def save(self, path: str | Path):
        """Persist the fitted vectorizer to models/vectorizers/."""
        with open(path, "wb") as f:
            pickle.dump(self.vectorizer, f)

    def load(self, path: str | Path):
        """Load a previously fitted vectorizer."""
        with open(path, "rb") as f:
            self.vectorizer = pickle.load(f)
        self._is_fitted = True
        return self
