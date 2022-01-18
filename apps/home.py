import streamlit as st
import os
import ee
import geemap


def app():
    st.title("Desertification Detection with Deep Learning and Satellite Data")

    st.header("Introduction")
    st.markdown(
        """
    Desertification is the persistent degradation of dryland ecosystems by 
    variations in climate and human activities.
    
    In other words it is making what used to be arable farming land into useless one. 
    It is one of the greatest environmental challenges today and unfortunately mostly targets the 
    world's poorest population.
    
    Desertification leads to so many other problems from affecting the agricultural sector leading to more 
    hunger, to increasing the displacement of people who used to live on these lands yields and what used 
    to be green fields, which in return have its own set of problems.

    Fortunately though, most of this degradation can be reversed and treated by many methods that’s why 
    many reports have been published addressing this important topic and demanding immediate actions. 
    It is also why most of the countries suffer from it, due to obvious disregard by the authorities of 
    these regions and countries.


    """
    )

    st.subheader("Research Problem")
    st.markdown(
        """
    -   According to recent reports, the rate of desertification in Iraq has increased to 39% and 54% of the country's agricultural land faces drought and land degradation.
    
    -   According to a report by the Republic of Iraq Ministry of Agriculture, Iraq is losing 100 square kilometers annually from its arable lands as a consequence of desertification.
    
    -   Iraq’s  highly excessive dependence on water that comes outside of its borders, the mismanagement of water, inefficient farming habits and the already dry climate makes it more vulnerable to climate change.
    
    -   Having more reliable sources to know where to focus the efforts could be the beginning of solving this huge challenge and provide immediate help to the most endangered regions.

    
    """
    )


    st.subheader("Project Goals")
    st.markdown(
        """
    AI has proven to provide more and more accurate forecast results in recent years, 
    allowing the formulation of solutions in a faster and agile way than before. 
    Here we’ll work to harvest this technological advancement to help predict the most 
    areas and regions that could fall victim to desertification in the upcoming years in Iraq.
    That is why for 6 weeks our goal will be to produce a forecasting model to predict the status 
    of different land covers in Iraq. 

        
    """
    )


    # with st.expander("Where to find your Earth Engine token?"):
    #     st.markdown(
    #         """
    #         - **Windows:** `C:/Users/USERNAME/.config/earthengine/credentials`
    #         - **Linux:** `/home/USERNAME/.config/earthengine/credentials`
    #         - **macOS:** `/Users/USERNAME/.config/earthengine/credentials`
    #         """
    #     )

    # st.header("Example")

    # with st.expander("See Source Code"):
    #     st.code(
    #         """        


    # # Import libraries
    # import ee
    # import geemap.foliumap as geemap

    # # Create an interactive map
    # Map = geemap.Map(plugin_Draw=True, Draw_export=False)
    # # Add a basemap
    # Map.add_basemap("TERRAIN")
    # # Retrieve Earth Engine dataset
    # dem = ee.Image("USGS/SRTMGL1_003")
    # # Set visualization parameters
    # vis_params = {
    #     "min": 0,
    #     "max": 4000,
    #     "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
    # }
    # # Add the Earth Engine image to the map
    # Map.addLayer(dem, vis_params, "SRTM DEM", True, 0.5)
    # # Add a colorbar to the map
    # Map.add_colorbar(vis_params["palette"], 0, 4000, caption="Elevation (m)")
    # # Render the map using streamlit
    # Map.to_streamlit()

    # ##############################################################

    # # Import libraries
    # import ee
    # import geemap.foliumap as geemap

    # # Create an interactive map
    # Map = geemap.Map(plugin_Draw=True, Draw_export=False)
    # # Add a basemap
    # Map.add_basemap("TERRAIN")
    # # Retrieve Earth Engine dataset
    # dem = ee.Image("USGS/SRTMGL1_003")
    # # Set visualization parameters
    # vis_params = {
    #     "min": 0,
    #     "max": 4000,
    #     "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
    # }
    # # Add the Earth Engine image to the map
    # Map.addLayer(dem, vis_params, "SRTM DEM", True, 0.5)
    # # Add a colorbar to the map
    # Map.add_colorbar(vis_params["palette"], 0, 4000, caption="Elevation (m)")
    # # Render the map using streamlit
    # Map.to_streamlit()
    
    #     """
    #     )
    

