import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from constants.regions import regions_dict, regions_list, get_key
from constants.amounts import amounts_dict, amounts_list
import plotly.express as px

APP_TITLE = 'Philippines Map'
APP_SUB_TITLE = 'Source: Philippines'

@st.cache_data(experimental_allow_widgets=True)
def display_map(region_type: str):

    map = folium.Map(location=[
        12.8797, 121.7740
    ], zoom_start=5, scrollWheelZoom=True, tiles='CartoDB positron')
    
    choropleth = folium.Choropleth(
        geo_data=regions_dict[region_type]['path'],
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

    # Load Data
    df_merged_data = pd.read_excel('data/spreadsheets/merged_data.xlsx')

    st.markdown("# Map page 🗺️")
    st.sidebar.markdown("# Map page 🗺️")

    region_type = st.sidebar.selectbox("Select Location Type", regions_list)
    amount_type = st.sidebar.selectbox("Select Amount Type", amounts_list)

    display_map(region_type)

    st.subheader(f'Region: {region_type}')

    selected_region = df_merged_data[df_merged_data['REGION'] == regions_dict[region_type]['value']]

    average_credit_amount = selected_region['AVERAGE_AMOUNT_Credit'].sum()
    average_debit_amount = selected_region['AVERAGE_AMOUNT_Debit'].sum()
    average_financial_amount = selected_region['AVERAGE_AMOUNT_Financial'].sum()
    average_incoming_amount = selected_region['AVERAGE_AMOUNT_Incoming'].sum()
    average_outgoing_amount = selected_region['AVERAGE_AMOUNT_Outgoing'].sum()
    average_total_amount = selected_region['AVERAGE_AMOUNT_Average'].sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric('Average Credit Amount', f'₱{average_credit_amount:,.2f}')

    with col2:
        st.metric('Average Debit Amount', f'₱{average_debit_amount:,.2f}')

    with col3:
        st.metric('Average Financial Amount', f'₱{average_financial_amount:,.2f}')

    with col1:
        st.metric('Average Incoming Amount', f'₱{average_incoming_amount:,.2f}')

    with col2:
        st.metric('Average Outgoing Amount', f'₱{average_outgoing_amount:,.2f}')

    with col3:
        st.metric('Average Total Amount', f'₱{average_total_amount:,.2f}')

    st.subheader(f'Barchart of {amount_type} Amounts by Region')

    amount_value = amounts_dict[amount_type]['value']
    df_region = df_merged_data[['REGION', amount_value]]
    df_region['REGION'] = df_region['REGION'].apply(lambda x: get_key(x))

    # Sorting options
    sort_option = st.radio("Sort by:", ("Value (Ascending)", "Value (Descending)"))

    sorted_df = df_region.sort_values(by=[amount_value], ascending=[sort_option == "Value (Ascending)"])

    # Plotly bar chart
    fig = px.bar(
        sorted_df, 
        x='REGION', 
        y=amount_value, 
        title=f'{amount_type} Amounts by Region',
        labels={'REGION': 'Region', amount_value: amount_type},
    )

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
