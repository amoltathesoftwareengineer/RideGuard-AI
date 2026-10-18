
import streamlit as st

from src.risk_rules import assess_trip_risk

st.set_page_config(
    page_title="RideGuard AI",
    page_icon="🚗",
    layout="wide",
)

st.title("🚗 RideGuard AI")
st.write("Rule-based trip safety analysis dashboard.")

st.subheader("Enter Trip Details")

col1, col2 = st.columns(2)

with col1:
    distance = st.number_input(
        "Trip distance (km)", min_value=0.0, value=10.0
    )
    duration = st.number_input(
        "Trip duration (minutes)", min_value=1, value=30
    )

with col2:
    night_trip = st.selectbox("Night-time trip?", ["No", "Yes"])
    incident = st.selectbox("Incident reported?", ["No", "Yes"])

if st.button("Analyze Trip"):
    result = assess_trip_risk(
        distance_km=distance,
        duration_minutes=duration,
        night_trip=(night_trip == "Yes"),
        incident_reported=(incident == "Yes"),
    )

    st.subheader("Trip Risk Summary")
    st.metric("Rule-based score", result["score"])
    st.write("**Risk indicator:**", result["level"])

    if result["reasons"]:
        st.write("**Triggered indicators:**")
        for reason in result["reasons"]:
            st.write(f"- {reason}")
    else:
        st.write("No configured indicators were triggered.")

    st.warning(
        "Prototype only. This score does not guarantee safety "
        "and is not a substitute for emergency services."
    )
