"""
Packaging file - lets the project be installed in editable mode:
    pip install -e .
This makes `from src.parsing import pdf_parser` etc. importable from
anywhere (tests, notebooks, scripts) without sys.path hacks.
"""
from setuptools import setup, find_packages

setup(
    name="resume-screening-system",
    version="0.1.0",
    description="AI-Powered Resume Screening & Candidate Ranking System",
    packages=find_packages(include=["src", "src.*"]),
    python_requires=">=3.9",
)
