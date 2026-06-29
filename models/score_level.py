def get_score_level(score):

    if score >= 85:
        return "🟢 Excellent Match"

    elif score >= 65:
        return "🔵 Good Match"

    elif score >= 45:
        return "🟡 Moderate Match"

    else:
        return "🔴 Weak Match"