# /app/components/navBar.py

import streamlit as st
from pathlib import Path

def load_css():
    css_file = Path(__file__).parent.parent / "assets/css/navBar.css"
    if css_file.exists():
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_navBar():
    # Load component-specific CSS
    load_css()

    html_content = """
        <h1>My Dashboard Title</h1>
    """

    # Render HTML in Streamlit
    st.markdown(html_content, unsafe_allow_html=True)
