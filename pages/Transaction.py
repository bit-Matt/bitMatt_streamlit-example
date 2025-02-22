import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from constants.regions import regions_dict, regions_list, get_key
from constants.amounts import amounts_dict, amounts_list
from constants.provinces import provinces_dict, get_key_province
import plotly.express as px

APP_TITLE = 'Average Transaction Amount per customer 🏦'
APP_SUB_TITLE = 'Source: https://github.com/faeldon/philippines-json-maps'

@st.cache_data(experimental_allow_widgets=True)
def display_map(df_region, df_province, region_type):

    st.markdown("### Choropleth Map")
    st.write("This map displays the average transaction amount per customer for different regions or provinces in the Philippines.")
    st.write("Each polygon represents a region or province, and the color intensity reflects the average transaction amount.")
    st.write("Hover over a polygon to see detailed information about the region or province, including average credit, debit, financial, incoming, and outgoing amounts, as well as the average total amount per customer.")
    st.write("You can select a specific region or province using the dropdown menu on the left.")
    st.write("The color scale indicates higher transaction amounts with darker colors.")


    map = folium.Map(location=[
        12.8797, 121.7740
    ], zoom_start=5, scrollWheelZoom=True, tiles='CartoDB positron')

    is_all = region_type == 'All Regions'
    all_regions = 'data/jsons/regions.geojson'
    geo_data = all_regions if is_all else regions_dict[region_type]['path']
    key_on = 'feature.properties.ADM1_EN' if is_all else 'feature.properties.ADM2_EN'
    key_column = 'REGION' if is_all else 'PROVINCE'

    if is_all: 
        mapped_df = df_region.copy()
        mapped_df['REGION'] = mapped_df['REGION'].apply(lambda x: get_key(x))
    else:
        mapped_df = df_province.copy()
        mapped_df['PROVINCE'] = mapped_df['PROVINCE'].apply(lambda x: provinces_dict[x])
    
 
    choropleth = folium.Choropleth(
        geo_data=geo_data,
        data=mapped_df,
        key_on=key_on,
        columns=(key_column, 'AVERAGE_AMOUNT_Average'),
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.8,
        line_color='black',
        name='Average Amount',
    ).add_to(map)


    custom_tooltip = """
    <h4>{name}</h4>
    <p>Average Credit Amount: {average_credit_amount}</p>
    <p>Average Debit Amount: {average_debit_amount}</p>
    <p>Average Financial Amount: {average_financial_amount}</p>
    <p>Average Incoming Amount: {average_incoming_amount}</p>
    <p>Average Outgoing Amount: {average_outgoing_amount}</p>
    <hr>
    <p><b>Average Total Amount: {average_total_amount}</b></p>
    """

    if is_all:
        df_indexed = df_region.set_index('REGION')
        for feature in choropleth.geojson.data['features']:
            region_name = feature['properties']['ADM1_EN']
            mapped_region_name = regions_dict[region_name]['value'] if region_name in regions_dict else ''
            average_credit_amount = df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Credit'] if mapped_region_name in list(df_indexed.index) else 0
            average_debit_amount = df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Debit'] if mapped_region_name in list(df_indexed.index) else 0
            average_financial_amount = df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Financial'] if mapped_region_name in list(df_indexed.index) else 0
            average_incoming_amount = df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Incoming'] if mapped_region_name in list(df_indexed.index) else 0
            average_outgoing_amount = df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Outgoing'] if mapped_region_name in list(df_indexed.index) else 0
            average_total_amount = df_indexed.loc[mapped_region_name, 'AVERAGE_AMOUNT_Average'] if mapped_region_name in list(df_indexed.index) else 0

            # Check if the value is zero and replace with "No data"
            average_credit_amount = "No data" if average_credit_amount == 0 else f'₱{average_credit_amount:,.2f}'
            average_debit_amount = "No data" if average_debit_amount == 0 else f'₱{average_debit_amount:,.2f}'
            average_financial_amount = "No data" if average_financial_amount == 0 else f'₱{average_financial_amount:,.2f}'
            average_incoming_amount = "No data" if average_incoming_amount == 0 else f'₱{average_incoming_amount:,.2f}'
            average_outgoing_amount = "No data" if average_outgoing_amount == 0 else f'₱{average_outgoing_amount:,.2f}'
            average_total_amount = "No data" if average_total_amount == 0 else f'₱{average_total_amount:,.2f}'

            tooltip_content = custom_tooltip.format(
                name=region_name,
                average_credit_amount=average_credit_amount,
                average_debit_amount=average_debit_amount,
                average_financial_amount=average_financial_amount,
                average_incoming_amount=average_incoming_amount,
                average_outgoing_amount=average_outgoing_amount,
                average_total_amount=average_total_amount,
            )
            feature['properties']['tooltip_content'] = tooltip_content

        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(['ADM1_EN', 'tooltip_content'], labels=False)
        )
    else: 
        df_indexed = df_province.set_index('PROVINCE')
        for feature in choropleth.geojson.data['features']:
            province_name = feature['properties']['ADM2_EN']
            mapped_province_name = get_key_province(province_name)
            print(province_name, mapped_province_name)
            average_credit_amount = df_indexed.loc[mapped_province_name, 'AVERAGE_AMOUNT_Credit'] if mapped_province_name in list(df_indexed.index) else 0
            average_debit_amount = df_indexed.loc[mapped_province_name, 'AVERAGE_AMOUNT_Debit'] if mapped_province_name in list(df_indexed.index) else 0
            average_financial_amount = df_indexed.loc[mapped_province_name, 'AVERAGE_AMOUNT_Financial'] if mapped_province_name in list(df_indexed.index) else 0
            average_incoming_amount = df_indexed.loc[mapped_province_name, 'AVERAGE_AMOUNT_Incoming'] if mapped_province_name in list(df_indexed.index) else 0
            average_outgoing_amount = df_indexed.loc[mapped_province_name, 'AVERAGE_AMOUNT_Outgoing'] if mapped_province_name in list(df_indexed.index) else 0
            average_total_amount = df_indexed.loc[mapped_province_name, 'AVERAGE_AMOUNT_Average'] if mapped_province_name in list(df_indexed.index) else 0

            # Check if the value is zero and replace with "No data"
            average_credit_amount = "No data" if average_credit_amount == 0 else f'₱{average_credit_amount:,.2f}' 
            average_debit_amount = "No data" if average_debit_amount == 0 else f'₱{average_debit_amount:,.2f}'
            average_financial_amount = "No data" if average_financial_amount == 0 else f'₱{average_financial_amount:,.2f}'
            average_incoming_amount = "No data" if average_incoming_amount == 0 else f'₱{average_incoming_amount:,.2f}'
            average_outgoing_amount = "No data" if average_outgoing_amount == 0 else f'₱{average_outgoing_amount:,.2f}'
            average_total_amount = "No data" if average_total_amount == 0 else f'₱{average_total_amount:,.2f}'

            
            tooltip_content = custom_tooltip.format(
                name=province_name,
                average_credit_amount=average_credit_amount,
                average_debit_amount=average_debit_amount,
                average_financial_amount=average_financial_amount,
                average_incoming_amount=average_incoming_amount,
                average_outgoing_amount=average_outgoing_amount,
                average_total_amount=average_total_amount,
            )
            feature['properties']['tooltip_content'] = tooltip_content

        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(['ADM1_EN', 'tooltip_content'], labels=False)
        )

    st_folium(map, width=800, height=500)

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # Load Data
    df_regions_data = pd.read_excel('data/spreadsheets/merged_data.xlsx')
    df_provinces_data = pd.read_excel('data/spreadsheets/merged_provinces.xlsx')


    region_type = st.sidebar.selectbox("Select Location Type", regions_list)
    amount_type = st.sidebar.selectbox("Select Amount Type", amounts_list)

    display_map(df_regions_data, df_provinces_data, region_type)


    if region_type != 'All Regions':
        st.markdown("### Selected Region/Province")
        st.write(f"You have selected {region_type}. Here are the average transaction amounts for this {region_type}:")

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
        

    st.markdown("### Bar Chart")
    st.write("This bar chart displays the average transaction amounts by region.")
    st.write("You can choose to sort the regions by value in ascending or descending order using the radio buttons.")
    st.write("Click on a region's bar to view more details.")

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
