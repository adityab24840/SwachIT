import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import random
from datetime import datetime, timedelta
from PIL import Image

# Page config
st.set_page_config(page_title="SwachIT – Smart Waste, Smarter Communities", layout="wide")

# --- HEADER / HERO ---
st.title("♻️ SwachIT: Smart Waste, Smarter Communities")
st.subheader("Cleanliness. Accountability. Community.")

col1, col2 = st.columns([1.2, 1])
with col1:
    st.markdown("""
    ### Why SwachIT?
    Public waste bins are often neglected — either overflowing or ignored. SwachIT empowers communities to **track, manage, and reward** responsible waste disposal.

    Whether you're in a metro with NFC phones or a village with RFID cards, SwachIT ensures **everyone can participate** in keeping their community clean.
    """)
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2909/2909769.png", width=250)

# --- FEATURES ---
st.markdown("## 🇮🇳 Why SwachIT Matters for India")

features = {
    "🏘️ Community-Based Waste Management": "Designed for both urban colonies and rural panchayats — supports local leadership and decentralized accountability.",
    
    "📉 Reduce Manual Scavenging": "Digital logging reduces unsafe, unhygienic handling of waste by sanitation workers — promoting dignity of labor.",
    
    "📲 NFC + RFID for Bharat": "Urban areas can use NFC + QR codes; rural areas can use RFID tags and LED indicators — no smartphone needed.",
    
    "🛑 Overflow Alerts for Panchayats": "Bins monitored in real-time — gram panchayat heads get alerts if bins go unserviced for >48 hours.",
    
    "🧹 Track Swachh Bharat Goals": "Aligned with SBM Urban & Rural KPIs — clean areas earn points, qualify for awards and funding.",
    
    "💰 ULB Integration & Rewards": "Citizen participation tracked by Urban Local Bodies (ULBs) — link to property tax rebates, water bill discounts.",
    
    "👵 Accessibility First": "Elder-friendly UI and voice prompts in local languages ensure inclusive access for all age groups.",
    
    "🚛 Optimize Waste Collection": "Track quantity + pickup frequency per locality — help municipal trucks avoid unnecessary trips or pileups."
}

for k, v in features.items():
    st.markdown(f"**{k}** – {v}")


# --- TECH STACK ---
st.markdown("## 🛠️ Technology Stack")
col3, col4 = st.columns(2)
with col3:
    st.markdown("""
    - Python + FastAPI
    - PostgreSQL / SQLite
    - RFID + ESP32 for rural bins
    - NFC for urban users
    - Streamlit for dashboard
    """)
with col4:
    st.markdown("""
    - Firebase / Supabase (optional)
    - E-Ink display (optional)
    - Low-power IoT syncing
    - QR fallback + manual register
    """)


# --- DASHBOARD SECTION ---
st.markdown("## 📺 Live Dashboard Preview")

# Generate mock data
today = datetime.today()
dates = [today - timedelta(days=i) for i in range(7)][::-1]
waste_volume = [random.randint(30, 80) for _ in range(7)]
active_users = random.randint(120, 180)
cleanliness_score = round(random.uniform(70, 95), 1)
user_points = random.randint(-20, 100)

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

# User toggle
st.markdown("### ✈️ Update Your Status")
is_away = st.toggle("I'm out of town")
if is_away:
    st.info("Your bin usage will be paused. No penalties will be applied.")
else:
    st.success("You're marked as active.")

# --- CTA ---
st.markdown("---")
st.markdown("### 🚀 Ready to build a cleaner community with SwachIT?")
st.button("Join the Pilot", type="primary")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("© 2025 SwachIT – Built at Hackathon | Team HackStreet Boys")
