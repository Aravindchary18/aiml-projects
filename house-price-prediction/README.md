House Price Prediction

Predict house prices using features such as size (sqft), number of rooms, and age with a Linear Regression model. This project demonstrates multi-feature regression, model training, and prediction pipelines using Python, NumPy, and scikit-learn.

Objective:
Estimate the price of a house based on key features and make predictions for new properties.

Model:

Type: Multiple Linear Regression
Library: scikit-learn
Input Features (X): Size (sqft), Rooms, Age (years)
Target (y): Price (USD)
Output: Predicted price for a given house


Key Skills Demonstrated:

Multi-variate regression modeling
Feature-target mapping and input handling
Using NumPy arrays for numerical computations
Model training with .fit() and predictions with .predict()
Clean, commented, production-ready code


Usage:

Install dependencies:
```bash
pip install numpy scikit-learn  
```  
2. Run the project:  
```bash
python house_price_prediction.py  
```  
3. Example prediction:  
```python
# Predict price for a new house  
new_house = np.array([[2000, 4, 2]])  
predicted_price = model.predict(new_house)  
print(predicted_price)  
  
Sample Data  
```python 
# Features: Size (sqft), Rooms, Age (years)  
# Target: Price (USD)  
  
X = [  
    [1000, 2, 5],  
    [1200, 3, 4],  
    [1500, 3, 6],  
    [1800, 4, 3]  
]  
  
y = [200000, 240000, 300000, 360000]  
```
Repository Structure:  
  
house-price-prediction/  
└── house_price_prediction.py  
  
Technologies & Libraries:  
  
-Python 3.x – Programming language  
-NumPy – Efficient array handling and numeric operations  
-scikit-learn – Linear Regression model  

Notes:

-The project demonstrates prediction for new inputs using the learned model.  
-Features (X) and target (y) are properly mapped, and the code is well-commented.  
-This project is professional and internship-ready, suitable for demonstrating practical regression skills.  


