import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.cluster import KMeans
import folium
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_folium import folium_static
# Load the dataset
@st.cache_data
def load_data(selected_data):
    selected_data += ".csv" 
    return pd.read_csv(selected_data)

# Train the model
@st.cache_data
def train_model(data):
    x = data[["Rainfall"]]
    y = data["Label"]
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    classifier = SVC(kernel='linear')
    classifier.fit(x_scaled, y)
    return classifier, scaler

# Make prediction
def make_prediction(model, scaler, rainfall_input):
    input_data = np.array([[rainfall_input]])  # Reshape input data
    input_standard = scaler.transform(input_data)  # Standardize input data
    prediction = model.predict(input_standard)
    return prediction[0]

# Load data

box = pd.read_csv('areas_list.csv')
box_data = box['Area'].unique().tolist()

selected_area = st.selectbox("Select an area : ", box_data)

data = load_data(selected_area)

# Train model
classifier, scaler = train_model(data)

# Streamlit UI
st.title('Rainfall Prediction Web App')

# User input
rainfall_input = st.number_input('Enter the rainfall intensity:', value=0.0, step=0.1)

# Make prediction
if st.button('Predict'):
    prediction = make_prediction(classifier, scaler, rainfall_input)
    if prediction == 0:
        st.write("Low risk of water logging")
        data = pd.read_csv('map.csv')
        
        # Create a dictionary to store location names and coordinates
        locations = {}
        
        # Iterate over the rows of the DataFrame to populate the dictionary
        area = selected_area
        for index, row in data.iterrows():
            if(row['Area'] == area):
                location = row['Area']
                latitude = row['Latitude']
                longitude = row['Longitude']
                locations[location] = (latitude, longitude)
        
        # Create a map centered around Chennai
        mymap = folium.Map(location=[13.0827, 80.2707], zoom_start=10)
        
        # Define the user-entered location
        user_location = (13.0827, 80.2707)  # Example user location
        
        # Add markers for all locations in the dataset
        for location, coords in locations.items():
            folium.Marker(coords, popup=location,icon=folium.Icon(color='green')).add_to(mymap)
        
        # Add a marker for the user-entered location
        folium.Marker(user_location, popup="User Location").add_to(mymap)
        
        # Display the map
        mymap
        mymap.save("my_map.html")
        folium_static(mymap)
        unsafe_allow_html=True
        
        
        import streamlit as st
        import webbrowser
        
        
        if st.button('View Map'):
        
            webbrowser.open_new_tab('my_map.html')
    else:
        st.write("High risk of water logging")
        data = pd.read_csv('map.csv')
        
        # Create a dictionary to store location names and coordinates
        locations = {}
        
        # Iterate over the rows of the DataFrame to populate the dictionary
        area = selected_area
        for index, row in data.iterrows():
            if(row['Area'] == area):
                location = row['Area']
                latitude = row['Latitude']
                longitude = row['Longitude']
                locations[location] = (latitude, longitude)
        
        # Create a map centered around Chennai
        mymap = folium.Map(location=[13.0827, 80.2707], zoom_start=10)
        
        # Define the user-entered location
        user_location = (13.0827, 80.2707)  # Example user location
        
        # Add markers for all locations in the dataset
        for location, coords in locations.items():
            folium.Marker(coords, popup=location,icon=folium.Icon(color='red')).add_to(mymap)
        
        # Add a marker for the user-entered location
        folium.Marker(user_location, popup="User Location", icon=folium.Icon(color='green')).add_to(mymap)
        
        # Display the map
        mymap
        mymap.save("my_map.html")
        folium_static(mymap)
        unsafe_allow_html=True
        
        
        import streamlit as st
        import webbrowser
        
        
        if st.button('View Map'):
        
            webbrowser.open_new_tab('my_map.html')