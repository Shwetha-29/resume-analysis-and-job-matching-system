import json
from pathlib import Path


def load_categories():
    """
    Load skill categories from data/skills.json.
    """

    skills_file = Path("data/skills.json")

    with open(skills_file, "r", encoding="utf-8") as file:
        return json.load(file)


CATEGORIES = load_categories()


def generate_dashboard(resume_keywords, job_keywords):
    """
    Generate category-wise dashboard statistics.
    """

    dashboard = {}

    for category, skills in CATEGORIES.items():

        required_skills = {
            skill.lower()
            for skill in skills
        }.intersection(job_keywords)

        if not required_skills:
            continue

        matched_skills = required_skills.intersection(
            resume_keywords
        )

        dashboard[category] = {

            "matched": len(matched_skills),

            "required": len(required_skills),

            "percentage": round(
                len(matched_skills)
                / len(required_skills)
                * 100
            )

        }

    return dashboard