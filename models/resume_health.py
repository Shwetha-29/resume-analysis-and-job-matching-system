def get_resume_health(score):
    """
    Return resume health information based on ATS score.
    """

    if score >= 80:

        return {
            "stars": "★★★★★",
            "title": "EXCELLENT",
            "status": "Excellent ATS Readiness",
            "color": "green"
        }

    elif score >= 60:

        return {
            "stars": "★★★★☆",
            "title": "GOOD",
            "status": "Good ATS Readiness",
            "color": "yellow"
        }

    elif score >= 40:

        return {
            "stars": "★★★☆☆",
            "title": "FAIR",
            "status": "Moderate ATS Readiness",
            "color": "orange"
        }

    else:

        return {
            "stars": "★☆☆☆☆",
            "title": "NEEDS WORK",
            "status": "Poor ATS Readiness",
            "color": "red"
        }