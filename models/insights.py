def generate_insights(
    score,
    resume_keywords,
    sections,
    missing
):

    insights = []

    # ATS Score
    if score >= 85:
        insights.append(
            "Excellent ATS compatibility. Your resume is well aligned with the job description."
        )

    elif score >= 70:
        insights.append(
            "Good ATS score. Adding a few more relevant skills could further improve your chances."
        )

    else:
        insights.append(
            "ATS score is relatively low. Consider adding more relevant technical skills from the job description."
        )

    # Programming Skills
    programming = {
        "python",
        "java",
        "c",
        "c++",
        "c#"
    }

    matched_programming = programming.intersection(resume_keywords)

    if len(matched_programming) >= 2:
        insights.append(
            "Strong programming foundation detected."
        )

    # Machine Learning
    ml = {
        "machine learning",
        "deep learning",
        "tensorflow",
        "keras",
        "numpy",
        "pandas",
        "scikit-learn"
    }

    if len(ml.intersection(resume_keywords)) >= 3:
        insights.append(
            "Strong Machine Learning profile identified."
        )

    # Cloud
    cloud = {
        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes"
    }

    if len(cloud.intersection(resume_keywords)) == 0:
        insights.append(
            "Cloud technologies are missing. Learning AWS or Docker can strengthen your resume."
        )

    # Backend
    backend = {
        "flask",
        "django",
        "fastapi",
        "node",
        "express"
    }

    if len(backend.intersection(resume_keywords)) == 0:
        insights.append(
            "No backend framework detected. Consider adding Flask or Django projects."
        )

    # Experience
    if not sections["Experience"].strip():
        insights.append(
            "No work experience section detected. Add internships or freelance work if available."
        )

    # Projects
    if sections["Projects"].strip():
        insights.append(
            "Projects section found. Practical projects improve resume quality."
        )

    # Certifications
    if sections["Certifications"].strip():
        insights.append(
            "Certifications strengthen your technical profile."
        )

    # Missing Skills
    if len(missing) >= 5:
        insights.append(
            "Several important skills required by the job are missing from the resume."
        )

    return insights