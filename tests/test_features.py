from src.features.tfidf_features import TfidfFeatureBuilder


def test_tfidf_feature_builder():
    docs = [
        "python machine learning tensorflow",
        "java spring boot",
        "python pandas numpy"
    ]

    builder = TfidfFeatureBuilder()

    matrix = builder.fit_transform(docs)

    assert matrix.shape[0] == 3
    assert matrix.shape[1] > 0