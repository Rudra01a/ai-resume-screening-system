"""
utils/  — cross-cutting concerns shared by every other package.

WHY THIS FOLDER EXISTS:
Logging setup, file IO helpers, and constants are needed by parsing/,
preprocessing/, extraction/, features/, similarity/, ranking/, and
reporting/ alike. Putting them here (instead of duplicating small helper
functions in every module) keeps the codebase DRY.
"""
