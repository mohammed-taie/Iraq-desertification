import streamlit as st
import geemap.foliumap as geemap
import ee


def app():

    st.title("Customize the default map")

    def _update_slider(width_value, height_value, zoom_value, lat_value, lon_value):
        st.session_state["width_slider"] = width_value
        st.session_state["height_slider"] = height_value
        st.session_state["zoom_slider"] = zoom_value
        st.session_state["lat_slider"] = lat_value
        st.session_state["lon_slider"] = lon_value

    if "width_slider" not in st.session_state:
        st.session_state["width_slider"] = 700
    if "height_slider" not in st.session_state:
        st.session_state["height_slider"] = 500
    if "zoom_slider" not in st.session_state:
        st.session_state["zoom_slider"] = 4
    if "lat_slider" not in st.session_state:
        st.session_state["lat_slider"] = 40
    if "lon_slider" not in st.session_state:
        st.session_state["lon_slider"] = -100

    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)

    width = col1.slider(
        "Map width", key="width_slider", min_value=100, max_value=1000, step=50
    )

    height = col2.slider(
        "Map height", key="height_slider", min_value=100, max_value=1000, step=50
    )

    zoom = col3.slider(
        "Zoom level", key="zoom_slider", min_value=1, max_value=18, step=1
    )

    lat = col4.slider(
        "Center latitude", key="lat_slider", min_value=36.0, max_value=48.0, step=0.1
    )

    lon = col5.slider(
        "Center longitude", key="lon_slider", min_value=26.0, max_value=38.0, step=0.1
    )

    st.button(
        "Reset",
        on_click=_update_slider,
        kwargs={
            "width_value": 700,
            "height_value": 500,
            "zoom_value": 6,
            "lat_value": 43,
            "lon_value": 33,
        },
    )



    # m = geemap.Map(center=[lat, lon], zoom=zoom)
    # m.to_streamlit(width=width, height=height)


    # Create an interactive map
    Map = geemap.Map()

    # Add a basemap
    Map.add_basemap("TERRAIN")

    # Define geometry point
    point = ee.Geometry.Point([43.6793, 33.2232])
    # .filterBounds(point) \

    # Retrieve Earth Engine dataset
    image = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
        .filterDate('2016-12-30', '2016-12-31') \
        .sort('CLOUD_COVER') \
        .first() \
        .select('B[1-7]')

    # Set visualization parameters
    vis_params = {
        'min': 0,
        'max': 4000,
        'bands': ['B5', 'B4', 'B3']
    }

    # Centers the map view on a given object
    # Map.centerObject(point, 6)

    # Add the Earth Engine image to the map
    Map.addLayer(image, vis_params, "Landsat-8")


    # lat = 43.6793
    # lon = 33.2232 
    
    # To center the map view at a given coordinates with the given zoom level
    Map.setCenter(lat, lon, zoom)
    
    # Render the map using streamlit
    Map.to_streamlit(width=width, height=height)
