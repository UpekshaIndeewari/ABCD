import streamlit as st
import json
from pathlib import Path

selected_module = st.session_state.get("selected_module")
selected_site = st.session_state.get("selected_site", "All")

def show_tile_view():
    # Load JSON data
    data_path = Path(__file__).parent.parent.parent / "data/data_excel.geojson"
    with open(data_path, "r") as f:
        geojson = json.load(f)

    # Fetch latest session state values dynamically
    selected_module = st.session_state.get("selected_module", "All")
    selected_site = st.session_state.get("selected_site", "All")

    # st.write("Selected Module:", selected_module)
    # st.write("Selected Site:", selected_site)

    features = geojson["features"]

    if selected_module != "All":
        features = [f for f in features if f["properties"]["module"] == selected_module]
    
    if selected_site != "All":
        features = [f for f in features if f["properties"]["site"] == selected_site]

   #Display tiles 
    cols_per_row = 3  # Number of tiles per row
    for i in range(0, len(features), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, feature in enumerate(features[i:i+cols_per_row]):
            props = feature["properties"]
            with cols[j]:
                st.image(props["gis_image_url"], use_container_width=True)
                st.markdown(f"**Site:** {props['site']}")
                st.markdown(f"**Module:** {props['module']}")
