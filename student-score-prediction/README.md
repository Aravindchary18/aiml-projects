# Student Score Prediction

Predict a student’s exam score based on the number of study hours using a **Linear Regression model**. This project demonstrates **single-feature regression**, model training, and prediction pipelines using **Python, NumPy, and scikit-learn**.

---

## Objective
Estimate a student’s exam score from study hours and make predictions for new inputs.

---

## Model
- **Type:** Linear Regression  
- **Library:** scikit-learn  
- **Input Feature (`X`):** Study hours  
- **Target (`y`):** Exam score  
- **Output:** Predicted score for a given number of study hours  

---

## Key Skills Demonstrated
- Single-feature regression modeling  
- Feature-target mapping and input handling  
- Using NumPy arrays for numerical computations  
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
python student_score_prediction.py
```
3. Example prediction:
```python
import numpy as np

# Predict score for a student who studied 6 hours

new_student = np.array([[6]])
predicted_score = model.predict(new_student)
print(predicted_score)

Sample Data :
# Feature: Study hours
X = [
    [1],
    [2],
    [3],
    [4],
    [5]
]

# Target: Exam scores
y = [50, 55, 65, 70, 80]
```

Repository Structure:
student-score-prediction/
└── student_score_prediction.py

Technologies & Libraries:

-Python 3.x – Programming language
-NumPy – Efficient array handling and numeric operations
-scikit-learn – Linear Regression model

Notes:
-This project demonstrates prediction for new inputs using the trained model.
-Feature (X) and target (y) are properly mapped, and the code is well-commented.
-The project is professional and internship-ready, suitable for showcasing practical regression skills.
