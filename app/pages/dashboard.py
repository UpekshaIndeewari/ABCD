# /app/pages/dashboard.py

import streamlit as st
from pathlib import Path
from app.components import sidePanel, mainPanel

# Helper functions
def load_css(file_name):
    css_file = Path(__file__).parent.parent / "assets/css" / file_name
    if css_file.exists():
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show_dashboard():
    # Load CSS
    load_css("dashboard.css")

    sidePanel.show_sidePanel()

    mainPanel.show_mainPanel()
