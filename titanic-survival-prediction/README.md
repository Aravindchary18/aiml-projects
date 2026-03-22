# 🚢 Titanic Survival Prediction — Machine Learning Web App

A professional end-to-end Machine Learning project that predicts passenger survival on the Titanic using a trained classification model and a Streamlit web interface. This project demonstrates data preprocessing, model training using scikit-learn, model persistence with joblib, and deployment-ready application development.

---

## 🔍 Project Objective

The goal of this project is to build a machine learning model that can predict whether a passenger would survive the Titanic disaster based on key input features such as passenger class, gender, age, and fare. The project also focuses on deploying the model as an interactive web application for real-time inference.

---

## 🧠 Machine Learning Approach

- Data preprocessing and feature engineering were performed using scikit-learn utilities  
- Multiple machine learning techniques from scikit-learn were explored during model development  
- A classification model was trained on Titanic dataset features  
- The trained model was serialized using joblib and loaded into the Streamlit app for inference  

---

## 🎯 Features Used for Prediction

- Passenger Class (Pclass)  
- Sex (Gender)  
- Age  
- Fare  

---

## 🖥️ Application Features

- Interactive web interface built with Streamlit  
- Real-time predictions based on user input  
- Simple UI with dropdowns, sliders, and numeric inputs  
- Instant classification output: Survived / Did Not Survive  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- scikit-learn  
- NumPy  
- joblib  

---

## 📂 Structure

Titanic Survival Prediction/
│
├── README.md               → Project overview, features, setup, and portfolio description
├── app.py                  → Streamlit web application (main entry point for deployment)
├── titanicproject.py       → Model training, preprocessing, and experimentation code
├── model.pkl               → Trained machine learning model used by the app
├── requirements.txt        → List of dependencies required to run/deploy the project
---

## 🚀 How to Run Locally

1. Clone the repository:

git clone https://github.com/Aravindchary18/AIML-Projects-Portfolio.git

2. Navigate to the project directory:

cd AIML-Projects-Portfolio

3. Install dependencies:

pip install -r requirements.txt

4. Run the application:

streamlit run app.py

---

## 🌐 Deployment

This application can be deployed using Streamlit Community Cloud by connecting this GitHub repository and selecting `app.py` as the main file.

---

## 📊 Output

- 1 → Survived  
- 0 → Did Not Survive  

---

## 👨‍💻 Author

- Name: Aravind Nannabattuni  
- GitHub: https://github.com/Aravindchary18  

---

## 📌 Key Highlights

- End-to-end machine learning pipeline  
- Real-time prediction web application  
- Integration of trained ML model with a UI  
- Clean and production-style project structure  
- Suitable for portfolio and recruiter showcase  

---

## ⚠️ Disclaimer

This project is developed for educational and portfolio purposes. The predictions are based on historical data and should not be considered as real-world survival predictions.
