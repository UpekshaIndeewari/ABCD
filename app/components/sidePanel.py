import streamlit as st
from pathlib import Path
import json
from base64 import b64encode


def load_css():
    css_file = Path(__file__).parent.parent / "assets/css/sidepanel.css"
    if css_file.exists():
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_sidePanel():
    # Load CSS
    load_css()

    # Load JSON data
    data_path = Path(__file__).parent.parent.parent / "data/data_excel.geojson"
    with open(data_path, "r") as f:
        geojson = json.load(f)


    # Sidebar content
    with st.sidebar:

        # Get unique modules for Dropdown 1
        modules = sorted(set(feature["properties"]["module"] for feature in geojson["features"]))

        
        # Initialize session state before creating the widget
        if "selected_module" not in st.session_state:
            st.session_state.selected_module = "All"

        selected_module = st.selectbox("Select Module:", ["All"] + modules, key="selected_module")
        
        # Get unique descriptions
        module_info = {}

        for feature in geojson["features"]:
            module = feature["properties"]["module"]
            description = feature["properties"]["description"]
            module_info[module] = description
            
        # Dynamic text below dropdown
        if selected_module == "All":
            st.sidebar.write("Please select a module to see details.")
        else:
            st.sidebar.write(module_info.get(selected_module))

        # Get unique sites for Dropdown 2
        if selected_module == "All":
            sites = sorted(set(feature["properties"]["site"] for feature in geojson["features"]))
        else:
            sites = sorted(set(feature["properties"]["site"] for feature in geojson["features"] if feature["properties"]["module"] == selected_module
        ))
        
        # Dropdown2
        if "selected_site" not in st.session_state:
            st.session_state.selected_site = "All"

        selected_site = st.selectbox("Select Site:", ["All"] + sites, key="selected_site")
        
        # Get unique site descriptions
        site_info = {}

        for feature in geojson["features"]:
            site = feature["properties"]["site"]
            x_coordinate = feature["properties"]["x_coordinate"]
            y_coordinate = feature["properties"]["y_coordinate"]
            site_info[site] = f"X Coordinate:{x_coordinate}, Y Coordinate:{y_coordinate}"

        # Dynamic text below dropdown
        if selected_site == "All":
            st.sidebar.write("Please select the site to see details.")
        else:
            st.sidebar.write(site_info.get(selected_site))











        st.markdown("---")

        st.markdown(
        """
        <h4 style="font-weight: bold">Contact Us</h4>

        <div id="contact-container">
            <div class="contact-block">
                <a href="mailto:marble-imagine-support@example.com" class="contact-item">
                    <div class="icon" id="contact-icon"></div>
                </a>
            </div>
            <div class="contact-block">
                <a href="tel:+1234567890" class="contact-item">
                    <div class="icon" id="phone-icon"></div>
                </a>
            </div>
            <div class="contact-block">
                <a href="tel:+1234567890" class="contact-item">
                    <div class="icon" id="linkedin-icon"></div>
                </a>
            </div>
        </div>

        <h4 style="font-weight: bold; margine-top: 40px">FAQ?</h4>
        """ , unsafe_allow_html=True)