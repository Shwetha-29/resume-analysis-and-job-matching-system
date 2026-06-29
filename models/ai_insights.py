def generate_ai_insights(
    resume_keywords,
    missing_skills,
    sections,
    predictions,
    score
):
    """
    Generate categorized AI insights.
    """

    resume = {skill.lower() for skill in resume_keywords}

    strengths = []
    recommendations = []
    career_advice = []

    projects = sections.get("Projects", "").strip()
    experience = sections.get("Experience", "").strip()
    certifications = sections.get("Certifications", "").strip()

    # ---------------------------------
    # ATS Score
    # ---------------------------------

    if score >= 80:

        strengths.append(
            "Excellent ATS score. Your resume is well optimized for the job description."
        )

    elif score >= 60:

        strengths.append(
            "Good ATS score. Your resume matches many of the required skills."
        )

    else:

        recommendations.append(
            "Tailor your resume more closely to the job description to improve ATS performance."
        )

    # ---------------------------------
    # Skill Groups
    # ---------------------------------

    ml_skills = {
        "machine learning",
        "tensorflow",
        "keras",
        "lstm",
        "random forest",
        "scikit-learn"
    }

    genai_skills = {
        "langchain",
        "openai",
        "rag",
        "prompt engineering",
        "vector database",
        "gen ai"
    }

    backend_skills = {
        "flask",
        "django",
        "fastapi"
    }

    cloud_skills = {
        "aws",
        "docker",
        "kubernetes"
    }

    # ---------------------------------
    # Machine Learning
    # ---------------------------------

    if len(ml_skills.intersection(resume)) >= 4:

        strengths.append(
            "Strong Machine Learning profile with practical experience in modern ML technologies."
        )

    # ---------------------------------
    # Generative AI
    # ---------------------------------

    if len(genai_skills.intersection(resume)) >= 3:

        strengths.append(
            "Hands-on Generative AI experience detected using modern LLM technologies."
        )

    # ---------------------------------
    # Projects
    # ---------------------------------

    if projects:

        strengths.append(
            "Projects demonstrate practical implementation of technical skills."
        )

    else:

        recommendations.append(
            "Add academic or personal projects to strengthen your resume."
        )

    # ---------------------------------
    # Experience
    # ---------------------------------

    if experience:

        strengths.append(
            "Internship or work experience strengthens your industry readiness."
        )

    else:

        recommendations.append(
            "Adding internship or freelance experience will improve your resume."
        )

    # ---------------------------------
    # Certifications
    # ---------------------------------

    if certifications:

        strengths.append(
            "Professional certifications enhance your technical credibility."
        )

    # ---------------------------------
    # Backend Skills
    # ---------------------------------

    if not backend_skills.intersection(resume):

        recommendations.append(
            "Learning Flask, Django or FastAPI would strengthen your backend development profile."
        )

    # ---------------------------------
    # Cloud Skills
    # ---------------------------------

    if not cloud_skills.intersection(resume):

        recommendations.append(
            "Learning AWS or Docker will improve your cloud engineering readiness."
        )

    # ---------------------------------
    # Missing Skills
    # ---------------------------------

    if missing_skills:

        recommendations.append(
            "Top missing job skills: "
            + ", ".join(
                skill.title()
                for skill in sorted(missing_skills)
            )
            + "."
        )

    # ---------------------------------
    # Career Advice
    # ---------------------------------

    if predictions:

        strengths_role = predictions[0]["role"]

        career_advice.append(
            f"Your strongest career match is {strengths_role} based on your current skill set."
        )

        if len(predictions) > 1:

            second_role = predictions[1]["role"]

            career_advice.append(
                f"You are also a competitive candidate for {second_role} roles."
            )

    return {

        "strengths": strengths,

        "recommendations": recommendations,

        "career_advice": career_advice

    }