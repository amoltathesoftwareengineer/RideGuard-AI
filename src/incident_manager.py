
from datetime import datetime, timezone


def create_incident(description, severity="Medium"):
    """Create a basic incident record."""
    allowed_severities = {"Low", "Medium", "High"}

    if severity not in allowed_severities:
        raise ValueError("Severity must be Low, Medium, or High.")

    description = description.strip()

    if not description:
        raise ValueError("Incident description cannot be empty.")

    return {
        "description": description,
        "severity": severity,
        "reported_at": datetime.now(timezone.utc).isoformat(),
        "status": "Open",
    }
