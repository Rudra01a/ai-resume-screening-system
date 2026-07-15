"""
src/  — the domain layer of the application.

Everything in this package is pure Python with no knowledge of Streamlit
or any UI framework. This is intentional (clean architecture): the
frontend/ layer imports from here, never the other way around, so the
NLP/ML core can be tested, reused in a CLI, or wrapped in an API without
any changes.
"""
