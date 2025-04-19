import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="BinWise Dashboard", layout="wide")

# Mock data
today = datetime.today()
dates = [today - timedelta(days=i) for i in range(7)][::-1]
waste_volume = [random.randint(30, 80) for _ in range(7)]
active_users = random.randint(120, 180)
cleanliness_score = round(random.uniform(70, 95), 1)
user_points = random.randint(-20, 100)

# Header
st.title("🗑️ BinWise – Smart Waste Dashboard")
st.caption("Real-time community bin usage metrics")

# KPI section
col1, col2, col3 = st.columns(3)
with col1:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=cleanliness_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Cleanliness Score"},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "green"}}
    ))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.metric(label="🎯 User Points", value=f"{user_points} pts", delta=f"{'+ve' if user_points >= 0 else '-ve'} behavior")

with col3:
    st.metric(label="👥 Active Users Today", value=f"{active_users}")

# Waste volume chart
st.markdown("### 🗑️ Waste Volume Collected (Last 7 Days)")
waste_df = pd.DataFrame({
    "Date": [d.strftime("%b %d") for d in dates],
    "Waste (kg)": waste_volume
})
st.line_chart(waste_df.set_index("Date"))

# User control section
st.markdown("### ✈️ Update Status")
is_away = st.toggle("I'm out of town")
if is_away:
    st.info("Your bin usage will be paused. No penalties will be applied.")
else:
    st.success("You're marked as active.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ by Team EcoTrackers | Hackathon 2025")

