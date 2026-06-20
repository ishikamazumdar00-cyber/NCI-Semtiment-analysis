import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="NCI Nagpur Analytics Dashboard",
    page_icon="🏥",
    layout="wide"
)

# HEADER
st.title("🏥 NCI Nagpur Patient Experience Analytics Dashboard")
st.caption("Google Reviews + Justdial Review Analytics")

# KPI CARDS
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Reviews", "525")
col2.metric("Google Reviews", "380")
col3.metric("Justdial Reviews", "145")
col4.metric("Duplicates", "23")

# SENTIMENT DISTRIBUTION
st.divider()

sentiment_data = pd.DataFrame({
    "Sentiment": ["Positive", "Neutral", "Negative"],
    "Count": [357, 63, 105]
})

fig = px.pie(
    sentiment_data,
    names="Sentiment",
    values="Count",
    title="Overall Sentiment Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# DEPARTMENT ANALYSIS
st.divider()

department_data = pd.DataFrame({
    "Department": [
        "Clinical Staff",
        "Support Staff",
        "Hygiene",
        "Infrastructure",
        "Technology"
    ],
    "Positive": [84, 61, 42, 48, 89],
    "Negative": [16, 39, 58, 52, 11]
})

fig2 = px.bar(
    department_data,
    x="Department",
    y=["Positive", "Negative"],
    barmode="group",
    title="NCI Sentiment Analysis"
)

st.plotly_chart(fig2, use_container_width=True)

# TOP PATIENT COMPLAINTS
st.divider()

complaints_data = pd.DataFrame({
    "Issue": [
        "Dirty Washrooms",
        "OPD Congestion",
        "Long Waiting Times",
        "Rude Reception Staff",
        "Delayed Discharge"
    ],
    "Mentions": [212, 187, 165, 142, 98]
})

fig3 = px.bar(
    complaints_data,
    x="Mentions",
    y="Issue",
    orientation="h",
    title="Top Patient Complaints"
)

st.plotly_chart(fig3, use_container_width=True)

# TOP POSITIVE MENTIONS
st.divider()

positive_data = pd.DataFrame({
    "Strength": [
        "Experienced Doctors",
        "Quality Treatment",
        "Helpful Nursing Staff",
        "Advanced Equipment",
        "Clean Wards"
    ],
    "Mentions": [240, 210, 185, 160, 145]
})

fig_positive = px.bar(
    positive_data,
    x="Mentions",
    y="Strength",
    orientation="h",
    title="Most Appreciated Services"
)

st.plotly_chart(fig_positive, use_container_width=True)

# HR ALERTS
st.divider()

st.subheader("HR & Operations Alerts")

col1, col2 = st.columns(2)

with col1:
    st.error("""
    Hygiene Department

    Negative Sentiment: 58%

    Status: Critical

    Recommended Action:
    Immediate sanitation audit and washroom maintenance review.
    """)

with col2:
    st.success("""
    Clinical Staff

    Positive Sentiment: 84%

    Status: Excellent

    Recommended Action:
    Consider recognition and reward programs for high-performing teams.
    """)

# MONTHLY TREND
st.divider()

st.subheader("Monthly Sentiment Trend")

trend_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sentiment Score": [78, 74, 71, 69, 66, 62]
})

fig4 = px.line(
    trend_data,
    x="Month",
    y="Sentiment Score",
    markers=True,
    title="Patient Satisfaction Trend"
)

st.plotly_chart(fig4, use_container_width=True)

# PLATFORM COMPARISON
st.divider()

st.subheader("Platform Comparison")

platform_data = pd.DataFrame({
    "Platform": ["Google", "Justdial"],
    "Positive": [72, 64],
    "Negative": [28, 36]
})

fig5 = px.bar(
    platform_data,
    x="Platform",
    y=["Positive", "Negative"],
    barmode="group",
    title="Google vs Justdial Sentiment"
)

st.plotly_chart(fig5, use_container_width=True)
