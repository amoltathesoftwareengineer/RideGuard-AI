
import pandas as pd


def create_trip_report(trips):
    """Convert trip analysis records into a report table."""
    columns = [
        "trip_id",
        "distance_km",
        "duration_minutes",
        "risk_score",
        "risk_level",
        "risk_reasons",
    ]

    if not trips:
        return pd.DataFrame(columns=columns)

    return pd.DataFrame(trips).reindex(columns=columns)


def summarize_risk(report):
    """Summarize the rule-based risk indicators in a report."""
    if report.empty:
        return {
            "total_trips": 0,
            "elevated_trips": 0,
            "moderate_trips": 0,
        }

    return {
        "total_trips": len(report),
        "elevated_trips": int(
            (report["risk_level"] == "Elevated").sum()
        ),
        "moderate_trips": int(
            (report["risk_level"] == "Moderate").sum()
        ),
    }
