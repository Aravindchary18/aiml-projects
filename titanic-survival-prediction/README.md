# 🚢 Titanic Survival Prediction — Machine Learning Web App

A professional end-to-end Machine Learning project that predicts passenger survival on the Titanic using a trained classification model and a Streamlit web interface. This project demonstrates data preprocessing, model training using scikit-learn, model evaluation, model persistence with joblib, and deployment-ready application development.

---

## 🌐 Live Demo: 

🔗
https://titanic-survival-prediction-aravind.streamlit.app

---

## 🔍 Project Objective

The goal of this project is to build a machine learning model that can predict whether a passenger would survive the Titanic disaster based on key input features such as passenger class, gender, age, and fare. The project also focuses on deploying the model as an interactive web application for real-time inference.

---

## 🧠 Machine Learning Approach

- Data preprocessing and feature engineering were performed using scikit-learn utilities  
- Multiple machine learning algorithms (Logistic Regression and Decision Tree) were implemented and evaluated  
- Models were compared using evaluation metrics such as accuracy, precision, recall, and F1-score  
- The best model was selected based on F1-score  
- The trained model was serialized using joblib and integrated into the Streamlit application for inference  

---

## 🎯 Features Used for Prediction

- Passenger Class (Pclass)  
- Sex (Gender)  
- Age  
- Fare  

---

## 📊 Model Performance

### 🔹 Logistic Regression
- Accuracy: 0.8603  
- Precision (class 1): 0.88  
- Recall (class 1): 0.73  
- F1-score (class 1): 0.80  

Confusion Matrix:
```
[[105   7] [ 18  49]]
```
---

### 🔹 Decision Tree
- Accuracy: 0.7989  
- Precision (class 1): 0.74  
- Recall (class 1): 0.72  
- F1-score (class 1): 0.73  

Confusion Matrix:
```
[[95 17] [19 48]]
```

---

### 🏆 Final Model Selection
- The best model was selected based on F1-score  
- Logistic Regression performed better and was chosen as the final model  

---

## 🖥️ Application Features

- Interactive web interface built with Streamlit  
- Real-time predictions based on user input  
- User-friendly input controls (dropdowns, sliders, number inputs)  
- Instant classification output:
  - 1 → Survived  
  - 0 → Did Not Survive  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- scikit-learn  
- NumPy  
- joblib  

---

## 📂 Project Structure

Titanic Survival Prediction/
├── README.md  
├── app.py  
├── model.pkl  
├── requirements.txt  
└── titanic_survival_prediction.py  

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

This application can be deployed using Streamlit Community Cloud by connecting the GitHub repository and selecting `app.py` as the main file.

---

## 👨‍💻 Author

- Name: Aravind Nannabattuni  
- GitHub: https://github.com/Aravindchary18  

---

## 📌 Key Highlights

- End-to-end machine learning pipeline from training to deployment  
- Model comparison using multiple algorithms  
- Evaluation using accuracy, precision, recall, and F1-score  
- Real-time prediction web application  
- Clean integration of trained ML model with Streamlit UI  
- Portfolio-ready project demonstrating practical ML skills  

---

## ⚠️ Disclaimer

This project is developed for educational and portfolio purposes only. The predictions are based on historical data and should not be considered as real-world survival predictions.
