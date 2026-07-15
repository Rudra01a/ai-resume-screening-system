"""
Shared file IO helpers: YAML config loading, directory listing.
"""
from pathlib import Path
import yaml


def load_yaml(path: str | Path) -> dict:
    """Load and parse a YAML file into a dict."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def list_resume_files(directory: str | Path, extensions: tuple = (".pdf", ".docx")) -> list[Path]:
    """Return all resume files in a directory matching the given extensions."""
    directory = Path(directory)
    return sorted(
        p for p in directory.iterdir()
        if p.is_file() and p.suffix.lower() in extensions
    )
