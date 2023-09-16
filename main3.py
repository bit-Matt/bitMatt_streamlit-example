# Data Source: https://public.tableau.com/app/profile/federal.trade.commission/viz/FraudandIDTheftMaps/AllReportsbyState
# US State Boundaries: https://public.opendatasoft.com/explore/dataset/us-state-boundaries/export/

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

APP_TITLE = 'Philippines Map'
APP_SUB_TITLE = 'Source: Philippines'


def display_map():

    map = folium.Map(location=[
        12.8797, 121.7740
    ], zoom_start=4, scrollWheelZoom=False, tiles='CartoDB positron')
    
    choropleth = folium.Choropleth(
        geo_data='data/jsons/regions.geojson',
        columns=('State Name', 'State Total Reports Quarter'),
        key_on='feature.properties.ADM1_EN',
        line_opacity=0.8,
        highlight=True
    )
    choropleth.geojson.add_to(map)

    st_map = st_folium(map, width=700, height=450)

    return ''


def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")


    #Load Data
    df_continental = pd.read_csv('data/AxS-Continental_Full Data_data.csv')


    #Display Filters and Map
    state_name = display_map()

     


if __name__ == "__main__":
    main()