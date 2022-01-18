import streamlit as st
from PIL import Image


def app():

    st.title("Iraq Map")

    st.header("Introduction")
    st.markdown(
        """
    The goal of this phase is to collect free and publicly available Satellite data that covers 
    Iraq over the years and in different seasons.
    
    """
    )

    st.markdown(""" ----- """)

    # insert image
    image0 = Image.open('basemap_iraq.png')
    st.image(image0, use_column_width=True)