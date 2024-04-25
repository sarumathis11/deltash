import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

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
    else:
        st.write("High risk of water logging")