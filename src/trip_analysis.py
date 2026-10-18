
from src.risk_rules import assess_trip_risk


def analyze_trip(trip):
    """Analyze one trip record using configured safety rules."""
    required_fields = [
        "distance_km",
        "duration_minutes",
        "night_trip",
        "incident_reported",
    ]

    for field in required_fields:
        if field not in trip:
            raise ValueError(f"Missing required field: {field}")

    distance = float(trip["distance_km"])
    duration = float(trip["duration_minutes"])

    if distance < 0 or duration <= 0:
        raise ValueError("Distance must be non-negative and duration positive.")

    return assess_trip_risk(
        distance_km=distance,
        duration_minutes=duration,
        night_trip=bool(trip["night_trip"]),
        incident_reported=bool(trip["incident_reported"]),
    )
