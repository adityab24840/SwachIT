import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="SwachIT – Smart Waste, Smarter Communities", layout="wide")

# Banner section
st.title("♻️ SwachIT: Smart Waste, Smarter Communities")
st.subheader("Cleanliness. Accountability. Community.")

# Hero section
col1, col2 = st.columns([1.2, 1])
with col1:
    st.markdown("""
    ### Why SwachIT?
    Public waste bins are often neglected — either overflowing or ignored. SwachIT empowers communities to **track, manage, and reward** responsible waste disposal.

    Whether you're in a metro with NFC phones or a village with RFID cards, SwachIT ensures **everyone can participate** in keeping their community clean.
    """)
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2909/2909769.png", width=250)

# Features section
st.markdown("## 🌟 Key Features")

features = {
    "📊 Usage Tracking": "Each household logs disposal using NFC or RFID — even without smartphones.",
    "🏅 Rewards & Penalties": "Earn points or discounts for regular participation. Slackers pay the price.",
    "📈 Waste Insights": "See real-time stats: how much waste, who’s active, and how clean your bin is.",
    "🧑‍🤝‍🧑 Participation Analytics": "Track how many households are using the system effectively.",
    "🌍 Offline Rural Mode": "RFID + microcontrollers allow low-cost, offline deployment in remote areas.",
}

for k, v in features.items():
    st.markdown(f"**{k}** – {v}")

# Dashboard preview
st.markdown("## 📺 Dashboard Preview")
st.image("https://user-images.githubusercontent.com/111914614/234302157-83792c20-3563-4405-a0fd-dde09f49dc99.png", caption="Sample Dashboard UI (mockup)")

# Tech stack
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

# Call to action
st.markdown("---")
st.markdown("### 🚀 Ready to build a cleaner community with SwachIT?")
st.button("Join the Pilot", type="primary")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("© 2025 SwachIT – Built at Hackathon | Team EcoTrackers")

