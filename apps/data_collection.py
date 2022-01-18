import ee
import streamlit as st
import geemap.foliumap as geemap
from PIL import Image


def app():
    
    # Page title
    st.title("Data collection")
    
    # # Header
    # st.header("Introduction")

    # # Time series analysis Definitoin
    # st.info("""
    #     **Time series analysis** is a specific way of analyzing a sequence of data 
    #     points collected over an interval of time.
    # """
    # )

    # # Methodology
    # st.markdown(
    #     """
    # This page will demostrate how we used time series analysis 
    # to predict NDVI condition over time. We used **Random Forst Regressor** to predict the numeric values.
    # Other options could be XGBoost, LightGBM, or Neural Networks for Multi-Outputs.
    
    # """
    # )
    
    # st.markdown(""" ----- """)

    # # Select Locations of Interest
    # st.subheader("Select Locations of Interest")

    # # insert image
    # image0 = Image.open('TSA_select_locations_of_interest.png')
    # st.image(image0, use_column_width=True)

    # st.markdown(""" ----- """)

    # # Select Locations of Interest - zooming in
    # st.subheader("Select Locations of Interest - zooming in")

    # # insert image
    # image1 = Image.open('TSA_select_Locations_of_Interest_zooming_in.png')
    # st.image(image1, use_column_width=True)

    # st.markdown(""" ----- """)


    # # Analyzing Desert Edges For Land Type Changes
    # st.subheader("Analyzing Desert Edges For Land Type Changes")

    # # insert image
    # image2 = Image.open('TSA_analyzing_desert_edges_for_land_type_changes.png')
    # st.image(image2, use_column_width=True)

    # st.markdown(""" ----- """)

    # # Example
    # st.header("Example")

    # # Explanation
    # st.markdown(
    #     """
    # We will use two locations in central Iraq with data from MODIS satellite, covering 20 years,
    # to predict NDVI values for five years.
    
    # """
    # )

    # # insert image
    # image3 = Image.open('TSA_NDVI_two_locations.png')
    # st.image(image3, use_column_width=True)
    

    # # Visualization of location 1
    # st.markdown(""" **Location 1:** """)

    # # insert image
    # image4 = Image.open('prediction_5_years_loc_1.jpg')
    # st.image(image4, use_column_width=True)

    # st.markdown(""" ----- """)

    # # Visualization of location 2
    # st.markdown(""" **Location 2:** """)

    # # insert image
    # image5 = Image.open('prediction_5_years_loc_2.png')
    # st.image(image5, use_column_width=True)
 
 