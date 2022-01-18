import ee
import streamlit as st
import geemap.foliumap as geemap
from PIL import Image


def app():

    # page title
    st.title("Supervised machine learning")

    # header
    st.markdown(
        """
    This task demostrates how we used supervised machine learning algorithms 
    to classify different land type covers. A summary of what has been done for this task is shown below:
    
    """
    )

    
    # Summary
    st.subheader("Summary")
    st.markdown(
        """
    1. Collected MODIS NDVI for April Month from 2000 to 2021
    
    2. Established Vegetation Condition Index by calculating from Long-term Maximum and Long-term Minimum 
    
    3. Used ESA 10 m Land Use and Land Cover  50 Agricultural points are Sampled and using those Sample point  to extract Vegetation Condition Index
    
    4. Used a Standardized Threshold of VCI < 40 is applied for Drought conditions and VCI> 40 for Non Drought Conditions.
    
    5. Calculated the Drought Frequency means whether a pixel is drought in particular year then the values are summed up for all the years to establish whether a point is drought or not.
    
    6. Used QGIS or Streamlit the Data has been published

    7. Used supervised learning methods were used to find drought vs non-drought areas

    """
    )

    st.markdown(""" ----- """)


    # 1. Selected points

    st.subheader("Selected points")
    st.markdown(
        """
        We selected a number of points in northern Iraq, in the area extending from northern borders 
        to Baghdad, to do our experiments.
    """
    )

    # map
    image0 = Image.open('selected_points.png')
    st.image(image0, use_column_width=True)
    st.markdown(""" ----- """)


    # Region of interest
    st.subheader("Region of interest")
    image1 = Image.open('SML_1.png')
    st.image(image1, use_column_width=True)
    st.markdown(""" ----- """)


    # Results & Visualizations
    st.subheader("Results & Visualizations")
    image2 = Image.open('SML_2.png')
    st.image(image2, use_column_width=True)
    st.markdown(""" ----- """)


    # Results & Visualizations
    st.subheader("Results & Visualizations")
    image2 = Image.open('SML_2.png')
    st.image(image2, use_column_width=True)
    st.markdown(""" ----- """)
    
    # Drought areas
    st.subheader("Results & Visualizations")
    image2 = Image.open('SML_2.png')
    st.image(image2, use_column_width=True)

