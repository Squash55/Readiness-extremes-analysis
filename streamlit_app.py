import streamlit as st
import pandas as pd

st.set_page_config(page_title="Readiness Extremes Analysis (Artificial data)", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("USAF_100_Base_Data.csv")

df = load_data()

st.title("📊 Readiness Extremes Analysis (Artificial data)")
st.markdown("Explore the top and bottom readiness scores across Air Force bases with their associated mission data.")

# Dropdown to select number of top/bottom entries
top_n = st.selectbox("Select number of top/bottom entries to display:", [5, 10, 20], index=1)

# Top readiness scores
st.subheader(f"🔝 Top {top_n} Readiness Scores")
df_top = df.sort_values(by="Readiness", ascending=False).head(top_n)
st.dataframe(df_top.reset_index(drop=True))

# Bottom readiness scores
st.subheader(f"🔻 Bottom {top_n} Readiness Scores")
df_bottom = df.sort_values(by="Readiness", ascending=True).head(top_n)
st.dataframe(df_bottom.reset_index(drop=True))

# Plain-language insight for bottom entries
st.subheader("🧠 Plain-Language Insights for Lowest Scores")
for i, row in df_bottom.iterrows():
    st.markdown(f"- **{row['Base']}** (Readiness: {row['Readiness']}) | Mission: {row['Mission']}, Maintenance Issues: {row['Maintenance Issues']}")

# Pattern insight for top scorers
most_common_top_mission = df_top["Mission"].mode()[0]
low_issue_count = (df_top["Maintenance Issues"] <= 2).sum()

st.subheader("🔎 Pattern Summary")
st.markdown(f"Most high-readiness scores are associated with the **{most_common_top_mission}** mission type.")
st.markdown(f"🛠️ {low_issue_count} out of {top_n} top bases have ≤2 maintenance issues.")
