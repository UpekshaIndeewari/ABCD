# /app/pages/dashboard.py

import streamlit as st
from pathlib import Path
from app.components import navBar, sidePanel, mainContent

# Helper functions
def load_css(file_name):
    css_file = Path(__file__).parent.parent / "assets/css" / file_name
    if css_file.exists():
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show_dashboard():
    # Load CSS
    load_css("dashboard.css")

    # Page layout using Streamlit columns
    left_col, right_col = st.columns([1, 5])

    # ------- LEFT COLUMN (Sidebar / Side Panel) -------
    with left_col:
        sidePanel.show_sidePanel()

    # ------- RIGHT COLUMN (Navbar + Main Content) -------
    with right_col:
        navBar.show_navBar()
        mainContent.show_mainContent()