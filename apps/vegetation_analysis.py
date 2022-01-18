import streamlit as st
from PIL import Image


def app():
    st.title("Vegetation Analysis")

    st.markdown(
        """
	The goal of this task is to discover the use of different vegetation indices to identify the level of 
    desertification in northern Iraq. Indices of interest include NDVI, NDWI, NDBI, and MSAVI. In specfic, we conducted the analysis using NDVI
    index, for the years 2016, 2018 and 2021. A summary of what has been done for this task is shown below:
    """
    )

    
    # Summary
    st.subheader("Summary")
    st.markdown(
        """
    1. **Dataset:** Sentinel2 images using Google Earth Engine

    2. **Region of Interest:** Mosul - Iraq

    3. **Periods of study:** 2016, 2018, 2021

    4. **Bands:** 5 Bands downloaded: R, G, B, NIR, SWIR

    5. **Processing method:** Used rasterio to process the images


    """
    )


    # NDVI analysis
    st.subheader("1. NDVI Analysis")

    # NDVI Definitoin
    st.info("""
        The normalized difference vegetation index (NDVI) is a simple graphical indicator that can be used to analyze remote sensing measurements, often from a space platform, 
        assessing whether or not the target being observed contains live green vegetation

    """
    )

    st.markdown(
        """
    The following shows NDVI values of Mosul for three different periods: 
    **2016**, **2018** and **2021**, calculated using data from Sentinel2.
    """
    )

    # NDVI_classes_2016
    st.markdown("""**NDVI: 2016**""")
    image1 = Image.open('NDVI_classes_2016.png')
    st.image(image1, use_column_width=True)
    
    st.markdown(""" ----- """)

    # NDVI_classes_2018
    st.markdown("""**NDVI: 2018**""")
    image2 = Image.open('NDVI_classes_2018.png')
    st.image(image2, use_column_width=True)

    st.markdown(""" ----- """)

    # NDVI_classes_2021
    st.markdown("""**NDVI: 2021**""")
    image3 = Image.open('NDVI_classes_2021.png')
    st.image(image3, use_column_width=True)


    # Pie chart Analysis
    st.subheader("2. Pie chart Analysis")

    st.markdown(
            """
        The following shows pie chart analysis of Mosul over three periods: 2016, 2018 and 2021.
        The results clearly show that the arid area is reducing and the green area is increasing, which seems to be a good indication.

        """
        )
    
    st.markdown("""**Pie chart analysis of Mosul: 2016**""")
    image2 = Image.open('NDVI_2016.png')
    st.image(image2, use_column_width=True)

    st.markdown(""" ----- """)

    st.markdown("""**Pie chart analysis of Mosul: 2018**""")
    image3 = Image.open('NDVI_2018.png')
    st.image(image3, use_column_width=True)

    st.markdown(""" ----- """)

    st.markdown("""**Pie chart analysis of Mosul: 2021**""")
    image3 = Image.open('NDVI_2021.png')
    st.image(image3, use_column_width=True)