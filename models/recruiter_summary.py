def generate_recruiter_summary(predictions, insights):
    """
    Generate recruiter-friendly executive summary.
    """

    summary = []

    # -------------------------
    # Strengths
    # -------------------------

    if predictions:

        top_role = predictions[0]["role"]

        if "Generative AI" in top_role:

            summary.append(
                "Strong profile in Generative AI and Machine Learning."
            )

        elif "Machine Learning" in top_role:

            summary.append(
                "Strong Machine Learning profile with practical project experience."
            )

        else:

            summary.append(
                "Strong technical profile with practical development experience."
            )

    # -------------------------
    # Best Career Match
    # -------------------------

    if predictions:

        summary.append(
            f"Best suited for {predictions[0]['role']} roles."
        )

    # -------------------------
    # Second Recommendation
    # -------------------------

    if len(predictions) > 1:

        summary.append(
            f"{predictions[1]['role']} is another strong career option."
        )

    # -------------------------
    # Improvement Advice
    # -------------------------

    for item in insights["recommendations"]:

        if "Docker" in item or "AWS" in item:

            summary.append(
                "Learning Docker and Cloud technologies will improve employability."
            )

            break

        elif "Flask" in item or "FastAPI" in item or "Django" in item:

            summary.append(
                "Backend development skills will significantly strengthen your profile."
            )

            break

    return summary