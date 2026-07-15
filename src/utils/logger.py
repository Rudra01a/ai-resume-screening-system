"""
Centralized logging setup, driven by config/logging.yaml.
Import get_logger(__name__) in any module instead of using print().
"""
import logging
import logging.config
from pathlib import Path

import yaml

_CONFIGURED = False


def _configure_logging(config_path: str = "config/logging.yaml"):
    global _CONFIGURED
    if _CONFIGURED:
        return

    config_path = Path(config_path)
    if config_path.exists():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        Path("outputs/logs").mkdir(parents=True, exist_ok=True)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    """Get a module-level logger, configuring logging on first call."""
    _configure_logging()
    return logging.getLogger(name)
