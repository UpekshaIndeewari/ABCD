# /app/components/expandButton.py

import streamlit as st
from pathlib import Path

def load_css():
    css_file = Path(__file__).parent.parent / "assets/css/expandButton.css"
    if css_file.exists():
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_expandButton():
    # Load component-specific CSS
    load_css()

    # Visible floating HTML button
    html_content = """
        <div id="expand-sidebar-btn">>></div>
    """

    st.markdown(html_content, unsafe_allow_html=True)
