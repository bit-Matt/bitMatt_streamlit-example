import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

APP_TITLE = 'Philippines Map'
APP_SUB_TITLE = 'Source: Philippines'



regionsDict = {
    'Region I': {
        'value': "REGION I (ILOCOS REGION)",
        "path": "data/jsons/region-1.geojson"
    },
    'Region II': {
        'value': "REGION II (CAGAYAN VALLEY)",
        "path": "data/jsons/region-2.geojson"
    },
    'Region III': {
        'value': "REGION III (CENTRAL LUZON)",
        "path": "data/jsons/region-3.geojson"
    },
    'Region IV-A': {
        'value': "MIMAROPA REGION",
        "path": "data/jsons/region-17.geojson"
    },
    'Region V': {
        'value': "REGION V (BICOL REGION)",
        "path": "data/jsons/region-5.geojson"
    },
    'Region VI': {
        'value': "REGION VI (WESTERN VISAYAS)",
        "path": "data/jsons/region-6.geojson"
    },
    'Region VII': {
        'value': "REGION VII (CENTRAL VISAYAS)",
        "path": "data/jsons/region-7.geojson"
    },
    'Region VIII': {
        'value': "REGION VIII (EASTERN VISAYAS)",
        "path": "data/jsons/region-8.geojson"
    },
    'Region IX': {
        'value': "REGION IX (ZAMBOANGA PENINSULA)",
        "path": "data/jsons/region-9.geojson"
    },
    'Region X': {
        'value': "REGION X (NORTHERN MINDANAO)",
        "path": "data/jsons/region-10.geojson"
    },
    'Region XI': {
        'value': "REGION XI (DAVAO REGION)",
        "path": "data/jsons/region-11.geojson"
    },
    'Region XII': {
        'value': "REGION XII (SOCCSKSARGEN)",
        "path": "data/jsons/region-12.geojson"
    },
    'Region XIII': {
        'value': "REGION XIII (CARAGA)",
        "path": "data/jsons/region-13.geojson"
    },
    'Cordillera Administrative Region': {
        'value': "CORDILLERA ADMINISTRATIVE REGION (CAR)",
        "path": "data/jsons/region-14.geojson"
    },
}

regions = list(regionsDict.keys())


def display_map(region_type: str):

    map = folium.Map(location=[
        12.8797, 121.7740
    ], zoom_start=5, scrollWheelZoom=True, tiles='CartoDB positron')
    
    choropleth = folium.Choropleth(
        geo_data=regionsDict[region_type]['path'],
        columns=('State Name', 'State Total Reports Quarter'),
        key_on='feature.properties.ADM1_EN',
        line_opacity=0.8,
        highlight=True
    )
    choropleth.geojson.add_to(map)

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['ADM2_EN'], labels=False)
    )

    st_folium(map, width=800, height=500)



def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    st.markdown("# Map page 🗺️")
    st.sidebar.markdown("# Map page 🗺️")

    region_type = st.sidebar.selectbox("Select Location Type", regions)


    state_name = display_map(region_type)

if __name__ == "__main__":
    main()
