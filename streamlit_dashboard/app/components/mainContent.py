# /app/components/mainContent.py

import streamlit as st
from pathlib import Path

def load_css():
    css_file = Path(__file__).parent.parent / "assets/css/mainContent.css"
    if css_file.exists():
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_mainContent():
    # Load component-specific CSS
    load_css()