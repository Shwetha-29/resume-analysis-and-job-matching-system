def calculate_weighted_score(skill_score, sections):
    """
    Calculate a weighted ATS score.

    Weights:
    Technical Skills : 70%
    Projects         : 10%
    Experience       : 10%
    Education        : 5%
    Certifications   : 5%
    """

    weights = {
        "Technical Skills": 0.70,
        "Projects": 0.10,
        "Experience": 0.10,
        "Education": 0.05,
        "Certifications": 0.05
    }

    breakdown = {
        "Technical Skills": round(skill_score),
        "Projects": 100 if sections.get("Projects", "").strip() else 0,
        "Experience": 100 if sections.get("Experience", "").strip() else 0,
        "Education": 100 if sections.get("Education", "").strip() else 0,
        "Certifications": 100 if sections.get("Certifications", "").strip() else 0
    }

    final_score = sum(
        breakdown[section] * weight
        for section, weight in weights.items()
    )

    return round(final_score, 2), breakdown