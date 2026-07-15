"""
Split a resume into logical sections (Education, Experience, Skills,
Projects, Certifications) using header-line regex matching.

Kept intentionally simple (regex, not ML) as a fast, dependency-free
baseline. A future improvement noted in roadmap: replace with a trained
sequence classifier if regex proves too brittle across resume formats.
"""
import re

SECTION_HEADERS = {
    "education": r"^\s*(education|academic background)\s*$",
    "experience": r"^\s*(experience|work experience|professional experience)\s*$",
    "skills": r"^\s*(skills|technical skills|key skills)\s*$",
    "projects": r"^\s*(projects|academic projects)\s*$",
    "certifications": r"^\s*(certifications|certificates)\s*$",
}


def segment_sections(text: str) -> dict[str, str]:
    """
    Split resume text into named sections based on header lines.

    Args:
        text: raw resume text with original line breaks preserved
              (call this BEFORE cleaner.clean_text collapses newlines).

    Returns:
        Dict mapping section name -> text content of that section.
        Content before the first recognized header is stored under "header".
    """
    lines = text.splitlines()
    sections: dict[str, list[str]] = {"header": []}
    current = "header"

    for line in lines:
        matched_section = None
        for name, pattern in SECTION_HEADERS.items():
            if re.match(pattern, line.strip(), flags=re.IGNORECASE):
                matched_section = name
                break

        if matched_section:
            current = matched_section
            sections.setdefault(current, [])
        else:
            sections.setdefault(current, []).append(line)

    return {name: "\n".join(content).strip() for name, content in sections.items()}
