import json
import re
from pathlib import Path


SKILLS_FILE = Path("data/skills.json")


def load_skills():
    """
    Load all skills from data/skills.json.
    """

    data = json.loads(SKILLS_FILE.read_text(encoding="utf-8"))

    return [
        skill.lower()
        for category in data.values()
        for skill in category
    ]


SKILLS = load_skills()


def extract_keywords(tokens):
    """
    Extract technical skills from text.
    Supports both single-word and multi-word skills.
    """

    text = " ".join(tokens).lower()

    found = set()

    for skill in SKILLS:
        pattern = rf"\b{re.escape(skill)}\b"

        if re.search(pattern, text):
            found.add(skill)

    return found


def compare_keywords(resume_keywords, job_keywords):
    """
    Compare resume skills with job description skills.
    """

    found = resume_keywords & job_keywords
    missing = job_keywords - resume_keywords

    score = (
        round((len(found) / len(job_keywords)) * 100, 2)
        if job_keywords
        else 0
    )

    return found, missing, score


def calculate_statistics(found, missing):
    """
    Generate statistics for dashboard cards.
    """

    return {
        "total": len(found) + len(missing),
        "found": len(found),
        "missing": len(missing),
    }