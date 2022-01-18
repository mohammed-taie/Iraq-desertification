import streamlit as st
from multiapp import MultiApp
from apps import home, timeseries, \
vegetation_analysis , basemap, supervised_learning

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here
apps.add_app("Home", home.app)
apps.add_app("Basemap", basemap.app)
apps.add_app("Vegetation analysis", vegetation_analysis.app)
apps.add_app("Supervised learning", supervised_learning.app)
apps.add_app("Time series analysis", timeseries.app)


# The main app
apps.run()
