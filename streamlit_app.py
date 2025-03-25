
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dynamic Readiness Interpreter (Artificial data)", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("USAF_100_Base_Data.csv")

df = load_data()

st.title("🧠 Dynamic Readiness Interpreter (Artificial data)")
st.markdown("Real-time plain-language analysis of readiness trends, issues, and mission patterns.")

# Key metrics
min_r = df["Readiness"].min()
max_r = df["Readiness"].max()
mean_r = df["Readiness"].mean()
median_r = df["Readiness"].median()
std_r = df["Readiness"].std()

st.subheader("📊 Readiness Stats")
st.markdown(f"**Readiness Range:** {min_r:.1f} to {max_r:.1f} | Mean: {mean_r:.1f} | Median: {median_r:.1f} | Std Dev: {std_r:.1f}")

# Outliers
low_outliers = df[df["Readiness"] < mean_r - std_r]
high_outliers = df[df["Readiness"] > mean_r + std_r]

st.subheader("📉 Notable Outliers")
st.markdown(f"- **{len(low_outliers)} bases** have unusually **low readiness** (< {mean_r - std_r:.1f})")
st.markdown(f"- **{len(high_outliers)} bases** show **exceptional readiness** (> {mean_r + std_r:.1f})")

# Mission patterns
low_mission_mode = low_outliers["Mission"].mode()[0] if not low_outliers.empty else "N/A"
high_mission_mode = high_outliers["Mission"].mode()[0] if not high_outliers.empty else "N/A"

st.subheader("🔎 Mission Pattern Insights")
st.markdown(f"- Among **low readiness** bases, the most common mission is **{low_mission_mode}**")
st.markdown(f"- Among **high readiness** bases, the most common mission is **{high_mission_mode}**")

# Maintenance correlation
low_maint_avg = low_outliers["Maintenance Issues"].mean() if not low_outliers.empty else 0
high_maint_avg = high_outliers["Maintenance Issues"].mean() if not high_outliers.empty else 0

st.subheader("🛠️ Maintenance Impact Summary")
st.markdown(f"- Average maintenance issues for **low readiness** bases: **{low_maint_avg:.1f}**")
st.markdown(f"- Average maintenance issues for **high readiness** bases: **{high_maint_avg:.1f}**")

# Summary
st.subheader("📋 Summary")
st.markdown(f"""
- Bases with **readiness below {mean_r - std_r:.1f}** may require urgent intervention.
- Mission type **{low_mission_mode}** appears frequently among underperformers.
- Lower readiness correlates with **higher average maintenance issues**.
- Recommend closer analysis of **maintenance drivers** and **mission planning** for {low_mission_mode} bases.
""")
