from models.skill_formatter import format_skill

ROLE_SKILLS = {

    "Machine Learning Engineer": {
        "python": 3,
        "machine learning": 5,
        "deep learning": 5,
        "tensorflow": 4,
        "keras": 3,
        "numpy": 2,
        "pandas": 2,
        "scikit-learn": 4,
        "data science": 3,
        "lstm": 5,
        "random forest": 4,
        "streamlit": 2,
        "streamlit cloud": 2,
        "gen ai": 2
    },

    "AI Engineer": {
        "python": 3,
        "langchain": 6,
        "langgraph": 5,
        "openai": 6,
        "prompt engineering": 6,
        "rag": 6,
        "vector database": 5,
        "llm": 5,
        "generative ai": 5,
        "gen ai": 5
    },

    "Generative AI Engineer": {
        "python": 3,
        "langchain": 6,
        "langgraph": 5,
        "openai": 6,
        "prompt engineering": 6,
        "rag": 6,
        "vector database": 5,
        "embeddings": 5,
        "transformers": 4
    },

    "Data Scientist": {
        "python": 3,
        "pandas": 3,
        "numpy": 3,
        "matplotlib": 2,
        "machine learning": 3,
        "data science": 4,
        "tensorflow": 3,
        "keras": 2,
        "random forest": 3,
        "lstm": 4,
        "sql": 2
    },

    "Python Backend Developer": {
        "python": 3,
        "flask": 5,
        "django": 5,
        "fastapi": 5,
        "rest api": 4,
        "sql": 2
    },

    "Full Stack Developer": {
        "html": 3,
        "css": 3,
        "javascript": 5,
        "react": 6,
        "node": 6,
        "express": 4,
        "rest api": 4,
        "git": 2,
        "github": 2,
        "responsive design": 2,
        "sql": 2
    },

    "Frontend Developer": {
        "html": 4,
        "css": 4,
        "javascript": 5,
        "react": 6,
        "responsive design": 4,
        "rest api": 3,
        "git": 2,
        "github": 2,
        "node": 2,
        "angular": 3,
        "vue": 3
    },

    "Database Engineer": {
        "sql": 4,
        "mysql": 4,
        "postgresql": 3,
        "mongodb": 3
    },

    "Cloud Engineer": {
        "aws": 5,
        "azure": 4,
        "gcp": 4,
        "docker": 5,
        "kubernetes": 5
    }

}


def get_match_level(score):

    if score >= 85:
        return "🟢 Excellent Match"

    elif score >= 70:
        return "🔵 Good Match"

    elif score >= 50:
        return "🟡 Moderate Match"

    return "🔴 Weak Match"


def predict_roles(
    resume_keywords,
    job_keywords,
    sections=None
):
    """
    Predict career roles using BOTH
    Resume Skills (70%)
    +
    Job Description Relevance (30%)
    """

    predictions = []

    resume_keywords = set(resume_keywords)
    job_keywords = set(job_keywords)

    for role, skills in ROLE_SKILLS.items():

        role_skills = set(skills.keys())

        # ------------------------------------
        # Skills from this role that are relevant
        # to the current job description
        # ------------------------------------

        relevant_role_skills = role_skills.intersection(job_keywords)

        # If none of this role's skills appear
        # in the job description, skip it.
        if len(relevant_role_skills) < 2:
            continue

        # -------------------------
        # Resume Fit
        # Only considers skills
        # relevant to this job
        # -------------------------

        total_weight = sum(
            skills[skill]
            for skill in relevant_role_skills
        )

        earned_weight = sum(
            skills[skill]
            for skill in relevant_role_skills
            if skill in resume_keywords
        )

        resume_score = (
            earned_weight / total_weight
        ) * 100

        # -------------------------
        # Job Score
        # -------------------------

        job_score = 100

        # -------------------------
        # Resume vs Job Match
        # -------------------------

        matched_job_skills = len(
            resume_keywords.intersection(job_keywords)
        )

        resume_job_score = (
            matched_job_skills / len(job_keywords)
        ) * 100

        # -------------------------
        # Bonus for high-value skills
        # -------------------------

        bonus = 0

        high_value = [
            "react",
            "node",
            "javascript",
            "python",
            "machine learning",
            "langchain",
            "rag",
            "tensorflow"
        ]

        for skill in high_value:

            if (
                skill in resume_keywords and
                skill in relevant_role_skills
            ):

                bonus += 2

        bonus = min(bonus, 10)

        # -------------------------
        # Final Score
        # -------------------------

        final_score = round(
            resume_score * 0.40 +
            job_score * 0.30 +
            resume_job_score * 0.20 +
            bonus,
            1
        )

        if final_score < 45:
            continue

        matched = [
            format_skill(skill)
            for skill in sorted(
                role_skills.intersection(resume_keywords)
            )
        ]

        missing = [
            format_skill(skill)
            for skill in sorted(
                role_skills - resume_keywords
            )
        ]

        matched_job = sorted(
            relevant_role_skills.intersection(resume_keywords)
        )

        top_skills = matched[:4]

        if top_skills:

            reason = (
                f"Strong match because your resume demonstrates "
                f"{', '.join(top_skills)}, "
                f"which are important skills for this role."
            )

        else:

            reason = (
                "Resume demonstrates transferable technical skills."
            )

        predictions.append({

            "role": role,

            "score": final_score,

            "level": get_match_level(final_score),

            "matched": matched,

            "missing": missing,

            "reason": reason

        })

    predictions.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return predictions[:5]