# /app/components/sidePanel.py

import streamlit as st
from pathlib import Path

def load_css():
    css_file = Path(__file__).parent.parent / "assets/css/sidepanel.css"
    if css_file.exists():
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_sidePanel():
    # Load component-specific CSS
    load_css()

    # Sidebar Content
    with st.container():
        st.sidebar.title("Navigation")
        st.sidebar.markdown("---")

        # Example navigation links (customize later)
        st.sidebar.write("🏠 Dashboard")
        st.sidebar.write("📊 Reports")
        st.sidebar.write("⚙️ Settings")