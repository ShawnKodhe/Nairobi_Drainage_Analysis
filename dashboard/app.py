import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px

from src.flood_risk import calculate_flood_risk
from src.drainage_priority import calculate_drainage_priority

# -------------------
# Dashboard Config
# -------------------
st.set_page_config(layout="wide", page_title="Nairobi Drainage Dashboard")
st.title("🌧 Nairobi Drainage Management Dashboard")
st.markdown("""
This dashboard helps Nairobi city planners and utility agencies **monitor drainage systems, assess flood risk, and prioritize maintenance**.
It combines historical rainfall data, drainage network status, and past flood reports into actionable insights.
""")

# -------------------
# Sidebar Filters
# -------------------
st.sidebar.header("Filters")
neighborhoods_list = pd.read_csv("data/neighborhoods.csv")["neighborhood"].tolist()
selected_neighborhoods = st.sidebar.multiselect("Select Neighborhood(s)", neighborhoods_list, default=neighborhoods_list)

# -------------------
# Tabs
# -------------------
tab1, tab2, tab3 = st.tabs(["Overview", "Flood Risk", "Drainage Priority"])

# -------------------
# Overview Tab
# -------------------
with tab1:
    st.header("🏙 Overview")
    st.markdown("""
    This overview provides a snapshot of **flood risk and drainage priorities** across Nairobi neighborhoods.
    Use the tabs above to explore detailed flood risk maps and drainage system priorities.
    """)
    flood_df = calculate_flood_risk()
    drain_df = calculate_drainage_priority()

    # Apply filter
    flood_df = flood_df[flood_df["neighborhood"].isin(selected_neighborhoods)]
    drain_df = drain_df[drain_df["neighborhood"].isin(selected_neighborhoods)]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Neighborhoods", len(flood_df))
    col2.metric("Top Flood Risk Score", round(flood_df["flood_risk_score"].max(), 2))
    col3.metric("Total Drains Monitored", len(drain_df))
    col4.metric("Top Drainage Priority Score", round(drain_df["priority_score"].max(), 2))

# -------------------
# Flood Risk Tab
# -------------------
with tab2:
    st.header("🌊 Flood Risk by Neighborhood")
    st.markdown("""
    The **flood risk score** is calculated using:
    - Average rainfall (mm)
    - Historical flood reports
    - Population density
    - Drainage blockage indicators
    """)
    st.dataframe(flood_df[["neighborhood", "flood_risk_score", "rainfall_mm", "flood_count", "population_density"]])

    fig = px.scatter_mapbox(
        flood_df,
        lat="lat",
        lon="lon",
        color="flood_risk_score",
        size="population",
        hover_name="neighborhood",
        hover_data=["rainfall_mm","flood_count","population_density"],
        zoom=10,
        mapbox_style="open-street-map",
        color_continuous_scale="reds",
        title="Flood Risk Map"
    )
    st.plotly_chart(fig, use_container_width=True)

    top_flood = flood_df.sort_values("flood_risk_score", ascending=False).head(5)
    st.subheader("Top 5 High-Risk Neighborhoods")
    st.table(top_flood[["neighborhood","flood_risk_score"]])

# -------------------
# Drainage Priority Tab
# -------------------
with tab3:
    st.header("🛠 Drainage Maintenance Priority")
    st.markdown("""
    The **drainage priority score** identifies drains that require urgent maintenance. It considers:
    - Drainage blockage
    - Neighborhood flood risk
    - Drain length
    """)
    st.dataframe(drain_df[["drain_id","neighborhood","status","blockage_score","priority_score"]])

    fig2 = px.scatter_mapbox(
        drain_df,
        lat="lat",
        lon="lon",
        color="priority_score",
        size="priority_score",
        hover_name="drain_id",
        hover_data=["neighborhood","status","blockage_score"],
        zoom=10,
        mapbox_style="open-street-map",
        color_continuous_scale="blues",
        title="Drainage Priority Map"
    )
    st.plotly_chart(fig2, use_container_width=True)

    top_drains = drain_df.sort_values("priority_score", ascending=False).head(5)
    st.subheader("Top 5 Drains Needing Maintenance")
    st.table(top_drains[["drain_id","neighborhood","priority_score","status"]])