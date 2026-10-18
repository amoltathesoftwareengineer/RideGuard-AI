
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RideGuard AI",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 RideGuard AI")
st.write("Ride safety monitoring and trip risk analysis dashboard.")

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
    night_trip = st.selectbox(
        "Night-time trip?", ["No", "Yes"]
    )
    incident_reported = st.selectbox(
        "Incident reported?", ["No", "Yes"]
    )

if st.button("Analyze Trip"):
    risk_score = 0
    reasons = []

    if duration > 0 and distance / duration * 60 > 100:
        risk_score += 2
        reasons.append("High average speed based on entered trip details")

    if night_trip == "Yes":
        risk_score += 1
        reasons.append("Night-time trip")

    if incident_reported == "Yes":
        risk_score += 2
        reasons.append("An incident was reported")

    if risk_score >= 3:
        level = "Elevated"
    elif risk_score >= 1:
        level = "Moderate"
    else:
        level = "Low based on configured rules"

    st.subheader("Trip Risk Summary")
    st.metric("Rule-based score", risk_score)
    st.write("**Indicator:**", level)

    if reasons:
        st.write("**Triggered indicators:**")
        for reason in reasons:
            st.write(f"- {reason}")
    else:
        st.write("No configured indicators were triggered.")

    st.caption(
        "Prototype only. This score does not guarantee safety "
        "and is not a substitute for emergency services."
    )
