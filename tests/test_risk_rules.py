
from src.risk_rules import assess_trip_risk


def test_low_risk_trip():
    result = assess_trip_risk(10, 30, False, False)

    assert result["score"] == 0
    assert result["level"] == "Low based on configured rules"


def test_night_trip_adds_indicator():
    result = assess_trip_risk(10, 30, True, False)

    assert result["score"] == 1
    assert "Night-time trip" in result["reasons"]


def test_incident_increases_score():
    result = assess_trip_risk(10, 30, False, True)

    assert result["score"] == 2
    assert "Incident reported" in result["reasons"]
