"""
Load ranking weights from config and validate they're sane (sum to 1,
no negative weights) before scoring runs.
"""
from src.utils.file_utils import load_yaml


def get_ranking_weights(config_path: str = "config/config.yaml") -> dict:
    """
    Load and validate ranking weights from config.yaml.

    Raises:
        ValueError: if weights are negative or don't sum to ~1.0.
    """
    config = load_yaml(config_path)
    weights = config["ranking"]["weights"]

    if any(w < 0 for w in weights.values()):
        raise ValueError(f"Ranking weights must be non-negative: {weights}")

    total = sum(weights.values())
    if not (0.99 <= total <= 1.01):
        raise ValueError(f"Ranking weights must sum to 1.0, got {total}: {weights}")

    return weights
