
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(page_title="3D Mission Readiness Analysis (Artificial data)", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("USAF_100_Base_Data.csv")

df = load_data()

st.title("🧭 3D Mission Readiness Analysis (Artificial data)")
st.markdown("Explore the impact of key variables on mission readiness using interactive 3D plots and golden insights.")

# Choose top 2 predictors for readiness
x_var = "Maintenance Issues"
y_var = "Personnel Gaps"
z_var = "Readiness"

# Fit a simple regression model for surface
X = df[[x_var, y_var]]
y = df[z_var]
model = LinearRegression()
model.fit(X, y)

# Create grid for surface
x_range = np.linspace(df[x_var].min(), df[x_var].max(), 30)
y_range = np.linspace(df[y_var].min(), df[y_var].max(), 30)
x_grid, y_grid = np.meshgrid(x_range, y_range)
z_pred = model.predict(np.c_[x_grid.ravel(), y_grid.ravel()]).reshape(x_grid.shape)

# Create 3D plot
fig = go.Figure()

# Regression surface
fig.add_trace(go.Surface(
    x=x_range, y=y_range, z=z_pred,
    colorscale="Viridis", opacity=0.5,
    name="Regression Surface"
))

# Data points
colors = df[z_var]
fig.add_trace(go.Scatter3d(
    x=df[x_var],
    y=df[y_var],
    z=df[z_var],
    mode='markers',
    marker=dict(
        size=6,
        color=colors,
        colorscale='RdYlGn',
        colorbar=dict(title="Readiness"),
        opacity=0.8
    ),
    text=df["Base"],
    hovertemplate="<b>%{text}</b><br>" + x_var + ": %{x}<br>" + y_var + ": %{y}<br>Readiness: %{z}<extra></extra>",
    name="Bases"
))

fig.update_layout(
    scene=dict(
        xaxis_title=x_var,
        yaxis_title=y_var,
        zaxis_title="Readiness"
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)

st.subheader("📈 3D Readiness Plot")
st.plotly_chart(fig, use_container_width=True)

# Golden questions + answers
st.subheader("💡 Golden Questions & Answers")
st.markdown("**Q1:** Which variables have the strongest impact on readiness?")
st.markdown("**A1:** Maintenance Issues and Personnel Gaps show the highest correlation with readiness.")

st.markdown("**Q2:** What pattern does the 3D plot reveal?")
st.markdown("**A2:** As maintenance issues and personnel gaps increase, readiness tends to decrease. Lower values cluster at the surface trough.")

st.markdown("**Q3:** Where are the highest-performing bases?")
st.markdown("**A3:** Bases with low maintenance and minimal personnel gaps appear in the green/blue high-readiness zone.")
