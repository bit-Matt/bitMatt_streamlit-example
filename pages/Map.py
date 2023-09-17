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
def display_map(df, region_type):

    map = folium.Map(location=[
        12.8797, 121.7740
    ], zoom_start=5, scrollWheelZoom=True, tiles='CartoDB positron')

    is_all = region_type == 'All Regions'
    all_regions = 'data/jsons/regions.geojson'
    geo_data = all_regions if is_all else regions_dict[region_type]['path']
    key_on = 'feature.properties.ADM1_EN' if is_all else 'feature.properties.ADM2_EN'
    
    choropleth = folium.Choropleth(
        data=df,
        geo_data=geo_data,
        key_on=key_on,
        columns=('REGION', 'AVERAGE_AMOUNT_Average'),
        line_opacity=0.8,
        highlight=True
    )
    choropleth.geojson.add_to(map)

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['ADM1_EN' if is_all else 'ADM2_EN'], labels=False)
    )

    if is_all:
        df_indexed = df.set_index('REGION')
        print(df_indexed.loc['REGION I (ILOCOS REGION)', 'AVERAGE_AMOUNT_Credit'])
        for feature in choropleth.geojson.data['features']:
            region_name = feature['properties']['ADM1_EN']
            mapped_region_name = regions_dict[region_name]['value'] if region_name in regions_dict else ''
            feature['properties']['average_credit_amount'] = 'Average Credit Amount: ' + '{:,}'.format(df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Credit']) if mapped_region_name in list(df_indexed.index) else ''
            feature['properties']['average_debit_amount'] = 'Average Debit Amount: ' + '{:,}'.format(df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Debit']) if mapped_region_name in list(df_indexed.index) else ''
            feature['properties']['average_financial_amount'] = 'Average Financial Amount: ' + '{:,}'.format(df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Financial']) if mapped_region_name in list(df_indexed.index) else ''
            feature['properties']['average_incoming_amount'] = 'Average Incoming Amount: ' + '{:,}'.format(df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Incoming']) if mapped_region_name in list(df_indexed.index) else ''
            feature['properties']['average_outgoing_amount'] = 'Average Outgoing Amount: ' + '{:,}'.format(df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Outgoing']) if mapped_region_name in list(df_indexed.index) else ''

        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(['ADM1_EN', 'average_credit_amount', 'average_debit_amount', 'average_financial_amount', 'average_incoming_amount', 'average_outgoing_amount'], labels=False)
        )

    st_folium(map, width=800, height=500)

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # Load Data
    df_regions_data = pd.read_excel('data/spreadsheets/merged_data.xlsx')

    st.markdown("# Map page 🗺️")
    st.sidebar.markdown("# Map page 🗺️")

    region_type = st.sidebar.selectbox("Select Location Type", regions_list)
    amount_type = st.sidebar.selectbox("Select Amount Type", amounts_list)

    display_map(df_regions_data, region_type)


    if region_type != 'All Regions':

        st.subheader(f'Region: {region_type}')

        selected_region = df_regions_data[df_regions_data['REGION'] == regions_dict[region_type]['value']]

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
    df_region = df_regions_data[['REGION', amount_value]]
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
