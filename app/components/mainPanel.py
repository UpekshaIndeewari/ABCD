import streamlit as st
import json
import folium
from streamlit_folium import st_folium
from pathlib import Path
from app.components import navBar, tileView

def load_css():
    css_file = Path(__file__).parent.parent / "assets/css/mainPanel.css"
    if css_file.exists():
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_mainPanel():
    load_css()
    navBar.show_navBar()

    # Tabs
    tab1, tab2 = st.tabs(["Tile View", "Map View"])

    with tab1:
        tileView.show_tile_view()

    with tab2:
        st.header("Map View")
        st.write("Interactive Map of Sites")

        # Load JSON data
        data_path = Path(__file__).parent.parent.parent / "data/data_excel.geojson"
        with open(data_path, "r") as f:
            geojson = json.load(f)

        # Center map roughly
        m = folium.Map(location=[51.5, 10.0], zoom_start=6)

        # Add markers
        for feature in geojson["features"]:
            props = feature["properties"]
            coords = feature["geometry"]["coordinates"]
            popup_html = f"""
            <b>Site:</b> {props['site']}<br>
            <b>Module:</b> {props['module']}<br>
            <img src="{props['gis_image_url']}" width="100">
            """
            folium.Marker(location=[coords[1], coords[0]],
                          popup=folium.Popup(popup_html, max_width=250)
                         ).add_to(m)

        # Display map
        st_folium(m, width=700, height=700)
