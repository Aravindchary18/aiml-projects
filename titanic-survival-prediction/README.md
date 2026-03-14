# Titanic Survival Prediction

Predict whether a passenger survived the Titanic disaster using a **Decision Tree Classifier**. This project demonstrates **classification**, handling categorical and numerical features, and prediction pipelines using **Python, NumPy, and scikit-learn**.

---

## Objective
Estimate passenger survival based on features like gender, age, and passenger class, and make predictions for new passengers.

---

## Model
- **Type:** Decision Tree Classifier  
- **Library:** scikit-learn  
- **Input Features (`X`):** Gender, Age, Passenger Class  
- **Target (`y`):** Survived (0 = No, 1 = Yes)  
- **Output:** Prediction of survival for a given passenger  

---

## Key Skills Demonstrated
- Classification modeling with decision trees  
- Handling categorical and numerical features  
- Mapping features (`X`) to target (`y`)  
- Model training with `.fit()` and predictions with `.predict()`  
- Clean, commented, production-ready code  

---

## Usage

1. **Install dependencies:**
```bash
pip install numpy scikit-learn
```

2. Run the project:
```bash
   python titanic_survival_prediction.py
```
3. Example prediction:
```
import numpy as np

# Predict survival for a new passenger: Female, Age 22, Class 3
new_passenger = np.array([[1, 22, 3]])  # 1 = Female, 0 = Male
predicted_survival = model.predict(new_passenger)
print(predicted_survival)  # Output: 0 or 1 
```
Sample Data:
```python
# Features: Gender (1=Female,0=Male), Age, Passenger Class
X = [
    [1, 22, 3],
    [0, 35, 1],
    [1, 28, 2],
    [0, 19, 3]
]

# Target: Survived (0=No, 1=Yes)
y = [1, 0, 1, 0]
```

Repository Structure:
titanic-survival-prediction/
└── titanic_survival_prediction.py

Technologies & Libraries:
-Python 3.x – Programming language
-NumPy – Efficient array handling and numeric operations
-scikit-learn – Decision Tree Classifier

Notes:
-This project demonstrates prediction for new passengers using the trained model.
-Feature (X) and target (y) are properly mapped, and the code is well-commented.
-The project is professional and internship-ready, suitable for showcasing practical classification skills.
