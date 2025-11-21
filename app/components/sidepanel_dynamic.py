import streamlit as st
from sidePanel import show_sidePanel
import json
from pathlib import Path

# Call the existing sidebar
show_sidePanel()

# Load geojson
data_path = Path(__file__).parent.parent / "data/data_excel.geojson"
with open(data_path, "r") as f:
    geojson = json.load(f)

# Build module -> description dictionary
module_descriptions = {
    feature["properties"]["module"]: feature["properties"]["description"]
    for feature in geojson["features"]
}

# Inject JS to dynamically update description under the existing HTML dropdown
module_desc_json = json.dumps(module_descriptions)

js_code = f"""
<script>
const moduleDescriptions = {module_desc_json};
const dropdown1 = document.getElementById('dropdown1');

// Create a paragraph below dropdown if not exists
let descParagraph = document.getElementById('module-description');
if (!descParagraph) {{
    descParagraph = document.createElement('p');
    descParagraph.id = 'module-description';
    descParagraph.style.marginTop = '10px';
    descParagraph.innerHTML = moduleDescriptions[dropdown1.value] || "No description available";
    dropdown1.parentNode.insertBefore(descParagraph, dropdown1.nextSibling);
}}

// Update description when dropdown changes
dropdown1.addEventListener('change', function() {{
    const selected = dropdown1.value;
    descParagraph.innerHTML = moduleDescriptions[selected] || "No description available";
}});
</script>
"""

st.markdown(js_code, unsafe_allow_html=True)
