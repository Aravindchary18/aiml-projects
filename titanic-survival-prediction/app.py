import os
import streamlit as st
import joblib 
import numpy as np


# Get the directory where this file (app.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the model file
model_path = os.path.join(BASE_DIR, "model.pkl")

# Load the trained machine learning model
model = joblib.load(model_path)

# App title
st.title("Titanic Survival Prediction")

# User inputs
# Passenger class selection
Pclass=st.selectbox("Passenger class",[1,2,3])

# Gender selection
Sex=st.selectbox("Sex",["Male","Female"])

# Age input using slider
Age=st.slider("Age",0,100,20)

# Fare input as numeric field
Fare=st.number_input("Fare",value=50)

# Convert categorical gender into numeric (model input format)
Sex = 0 if Sex=="Male" else 1

# Prediction button
if st.button("Predict"):
     
   # Prepare input in the format expected by the model
   input_data=np.array([[Pclass,Sex,Age,Fare]])

   # Make prediction
   prediction=model.predict(input_data)

   
   # Display result
   if prediction[0]==1:
      st.success("Survived")
   else:
      st.error("Did Not Survive")
      
