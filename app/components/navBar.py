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
    <div class="navbar-container">
        <div class="navbar-left">
            <a href="https://www.marble-imaging.de/">
                <img src="https://raw.githubusercontent.com/UpekshaIndeewari/ABCD/main/mi_logo_blue.png" class="navbar-milogo">
            </a>
        </div>
        <div class="navbar-center">
            <img src="https://raw.githubusercontent.com/UpekshaIndeewari/ABCD/main/pcis_logo.png" class="navbar-logo">
            <h3 class="navbar-title">Precious Coast Information System (PCIS)</h3>
        </div>
        <div class="nav-analytics">
            <a href="#">
                <img class="analytic-logo" src="https://raw.githubusercontent.com/UpekshaIndeewari/ABCD/main/analytics-svgrepo-com.png">
                <div class="analytic">My Analytics</div>
            </a>
        </div>
        <div class="nav-user">
            <a href="#">
                <img class="user-logo" src="https://raw.githubusercontent.com/UpekshaIndeewari/ABCD/main/user-svgrepo-com.png">
                <div class="user">User</div>
            </a>
        </div>
    </div>
    """

    # Render HTML in Streamlit
    st.markdown(html_content, unsafe_allow_html=True)
