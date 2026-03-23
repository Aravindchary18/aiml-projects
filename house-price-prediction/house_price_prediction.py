# Import required libraries

import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import joblib as jb


# Load dataset
df=pd.read_csv("train.csv")


# Select important features and target
X=df[["GrLivArea","BedroomAbvGr","YearBuilt","OverallQual","FullBath","GarageCars"]]
y=df["SalePrice"]


# Split data into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=19)


# Create Linear Regression model
model=LinearRegression()

# Train the model
model.fit(X_train,y_train)

# Make predictions on test data
y_pred=model.predict(X_test)

# Evaluate model performance
rmse=np.sqrt(mean_squared_error(y_test,y_pred))

r2=r2_score(y_test,y_pred)


# Print results
print("RMSE:",rmse)
print("R2 score:",r2)

# Save trained model
jb.dump(model,"house_model.pkl")
