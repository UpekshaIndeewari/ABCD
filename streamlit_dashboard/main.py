# main.py

import streamlit as st
from pathlib import Path
from app.pages import dashboard

# Load global CSS
global_css_file = Path(__file__).parent / "app/assets/css/global.css"
with open(global_css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="Marble Imagine | Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Run the dashboard page
dashboard.show_dashboard()