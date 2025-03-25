import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mission Readiness Explorer (Artificial data)", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("USAF_100_Base_Data.csv")

df = load_data()

st.title("📊 Mission Readiness Explorer (Artificial data)")
st.markdown("Explore mission readiness metrics using synthetic data from 100 simulated Air Force bases.")

# Summary stats
st.subheader("🔍 Summary Statistics")
st.dataframe(df.describe())

# Readiness histogram
st.subheader("📈 Readiness Distribution")
fig, ax = plt.subplots(figsize=(8, 4))  # Resized plot
ax.hist(df["Readiness"], bins=20, color="skyblue", edgecolor="black")
ax.set_xlabel("Readiness Score")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Readiness Scores")
st.pyplot(fig)

# Interpretation
st.markdown("**Interpretation:** Most readiness scores fall between 60 and 90, indicating moderate operational health. Outliers below 60 may indicate urgent issues at specific bases.")

# Maintenance bar chart
st.subheader("🔧 Maintenance Issues")
fig2, ax2 = plt.subplots(figsize=(8, 4))  # Resized plot
df["Maintenance Issues"].value_counts().sort_index().plot(kind="bar", color="orange", ax=ax2)
ax2.set_xlabel("Issue Level")
ax2.set_ylabel("Number of Bases")
ax2.set_title("Maintenance Issues Across Bases")
st.pyplot(fig2)

# Interpretation
st.markdown("**Interpretation:** The most frequent maintenance levels are between 2–4. Bases with 6+ issues are at higher risk of readiness degradation and may need immediate attention.")

# Readiness score formula and tooltips
st.subheader("🧮 Readiness Score Formula (Synthetic)")
st.markdown("**Readiness = 100 - (Mission Impact Score + Maintenance Issues Weighted + Personnel Gaps)**")

st.subheader("🛠️ Maintenance Issue Levels Explained")
st.markdown(\"""
- **0–2 (Low):** Minor or negligible impact  
- **3–5 (Moderate):** Operational caution advised  
- **6+ (High):** Significant risk to mission capability
\""")
