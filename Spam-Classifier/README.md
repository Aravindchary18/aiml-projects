# 📩 SMS Spam Classifier — Machine Learning Web App

A professional end-to-end Machine Learning project that classifies SMS messages as Spam or Not Spam (Ham) using a trained classification model and a Streamlit web interface. This project demonstrates text preprocessing, feature extraction using TF-IDF, model training with scikit-learn, evaluation, model persistence, and deployment-ready application development.

---

## 🌐 Live Demo:

🔗 https://spam-classifier-aravind-19.streamlit.app

---

## 🔍 Project Objective

The goal of this project is to build a machine learning model that can accurately classify SMS messages as spam or not spam based on their textual content. The project also focuses on deploying the trained model as an interactive web application for real-time predictions.

---

## 🧠 Machine Learning Approach

- Text preprocessing and label encoding were performed using pandas  
- TF-IDF (Term Frequency–Inverse Document Frequency) was used for feature extraction  
- Logistic Regression was used as the classification algorithm  
- Model performance was evaluated using Accuracy, F1-score, and Confusion Matrix  
- The trained model and vectorizer were serialized using pickle for reuse  
- The model was integrated into a Streamlit application for real-time inference  

---

## 🎯 Features Used for Prediction

- SMS Text Content  

---

## 📊 Model Performance

- Accuracy: ~96%  
- F1 Score: ~0.84  

---

Confusion Matrix:
[[953   0] [ 44 118]]

---

## 🖥️ Application Features

- Interactive web interface built with Streamlit  
- Real-time spam detection based on user input  
- Simple and user-friendly UI  
- Instant classification output:
  - 1 → Spam  
  - 0 → Not Spam (Ham)  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- scikit-learn  
- pandas  
- pickle  

---

## 📂 Project Structure

spam-classifier/
├── README.md  
├── SMS_SPAM_CLASSIFIER.py  
├── spam_app.py  
├── model.pkl  
├── vectorizer.pkl  
├── spam.csv  
├── requirements.txt  

---

---

## 🚀 How to Run Locally

1. Clone the repository:
git clone https://github.com/Aravindchary18/AIML-Projects-Portfolio.git⁠�

2. Navigate to the project directory:
cd AIML-Projects-Portfolio/spam-classifier

3. Install dependencies:
pip install -r requirements.txt

4. Run the application:
streamlit run spam_app.py

---

## 🌐 Deployment

This application is deployed using Streamlit Community Cloud by connecting the GitHub repository and selecting `spam_app.py` as the main file.

---

## 👨‍💻 Author

- Name: Aravind Nannabattuni  
- GitHub: https://github.com/Aravindchary18  

---

## 📌 Key Highlights

- End-to-end machine learning pipeline from preprocessing to deployment  
- TF-IDF based text feature extraction  
- Logistic Regression model for classification  
- Evaluation using Accuracy, F1-score, and Confusion Matrix  
- Real-time prediction web application using Streamlit  
- Clean integration of ML model with user interface  
- Portfolio-ready project demonstrating practical ML and basic NLP skills  

---

## ⚠️ Disclaimer

This project is developed for educational and portfolio purposes only. Predictions are based on trained data and may not generalize perfectly to all real-world SMS messages.
