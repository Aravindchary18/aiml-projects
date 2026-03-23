# Import required libraries
import streamlit as st
import joblib
import numpy as np
import os

# Load trained model from current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "house_model.pkl"))

# App title
st.title("🏡 House Price Prediction 🏘️")

# User input fields
Area = st.number_input("Area (GrLivArea)", min_value=1, max_value=10000)
Bedroom = st.number_input("Bedrooms (BedroomAbvGr)", min_value=1, max_value=7, step=1)
Year = st.number_input("Year Built", min_value=1800, max_value=2025)
Quality = st.number_input("Overall Quality (1-10)", min_value=1, max_value=10)
Bathrooms = st.number_input("Full Bathrooms", min_value=0, max_value=10)
Garage = st.number_input("Garage Cars", min_value=0, max_value=10)

# Prediction button
if st.button("Predict"):
    # Prepare input data for model
    input_data = np.array([[Area, Bedroom, Year, Quality, Bathrooms, Garage]])

    # Predict house price
    prediction = model.predict(input_data)[0]

    # Ensure price is not negative
    prediction = max(0, prediction)

    # Display result
    st.success(f"Predicted Price: {prediction:.2f}")