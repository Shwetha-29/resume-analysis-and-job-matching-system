def get_progress_color(score):
    """
    Return a Bootstrap-like color class
    based on the percentage score.
    """

    if score >= 80:
        return "green"

    elif score >= 60:
        return "yellow"

    elif score >= 40:
        return "orange"

    return "red"