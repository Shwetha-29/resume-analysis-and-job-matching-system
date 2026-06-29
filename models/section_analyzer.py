import re


SECTION_PATTERNS = {
    "Education": r"\bEDUCATION\b",
    "Skills": r"\bSKILLS\b",
    "Projects": r"\bPROJECTS\b",
    "Experience": r"\bEXPERIENCE\b",
    "Certifications": r"\bCERTIFICATION(?:S)?\b",
    "Languages": r"\bLANGUAGES\b"
}


def analyze_sections(text):
    """
    Extract resume sections using regex.
    Works better with PDFs where headings may appear on the same line.
    """

    # Normalize whitespace
    text = re.sub(r"\r", "", text)
    text = re.sub(r"[ \t]+", " ", text)

    matches = []

    # Locate all section headings
    for section, pattern in SECTION_PATTERNS.items():

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            matches.append(
                (match.start(), match.end(), section)
            )

    if not matches:
        return {
            section: ""
            for section in SECTION_PATTERNS
        }

    matches.sort()

    sections = {}

    for index, (_, end, section_name) in enumerate(matches):

        next_start = (
            matches[index + 1][0]
            if index < len(matches) - 1
            else len(text)
        )

        sections[section_name] = text[
            end:next_start
        ].strip()

    # Fill any missing sections
    for section in SECTION_PATTERNS:
        sections.setdefault(section, "")

    return sections