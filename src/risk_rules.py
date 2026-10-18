
def assess_trip_risk(distance_km, duration_minutes, night_trip, incident_reported):
    """Calculate a simple rule-based trip risk indicator."""
    score = 0
    reasons = []

    if duration_minutes > 0:
        average_speed = distance_km / duration_minutes * 60

        if average_speed > 100:
            score += 2
            reasons.append("High calculated average speed")

    if night_trip:
        score += 1
        reasons.append("Night-time trip")

    if incident_reported:
        score += 2
        reasons.append("Incident reported")

    if score >= 3:
        level = "Elevated"
    elif score >= 1:
        level = "Moderate"
    else:
        level = "Low based on configured rules"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }
