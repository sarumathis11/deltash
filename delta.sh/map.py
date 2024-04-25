import pandas as pd
from sklearn.cluster import KMeans
import folium
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_folium import folium_static

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('map.csv')

# Create a dictionary to store location names and coordinates
locations = {}

# Iterate over the rows of the DataFrame to populate the dictionary
for index, row in data.iterrows():
    location = row['Area']
    latitude = row['Latitude']
    longitude = row['Longitude']
    locations[location] = (latitude, longitude)

# Create a map centered around Chennai
mymap = folium.Map(location=[13.0827, 80.2707], zoom_start=10)

# Define the user-entered location
user_location = (latitude, longitude)  # Example user location

# Add markers for all locations in the dataset
for location, coords in locations.items():
    folium.Marker(coords, popup=location).add_to(mymap)

# Add a marker for the user-entered location
folium.Marker(user_location, popup="User Location", icon=folium.Icon(color='red')).add_to(mymap)

# Display the map
mymap
mymap.save("my_map.html")
folium_static(mymap)
unsafe_allow_html=True






import streamlit as st
import webbrowser


if st.button('View Map'):
 
    webbrowser.open_new_tab('my_map.html')

