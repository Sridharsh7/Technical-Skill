# -*- coding: utf-8 -*-
"""Fitness tracking system.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DLAb3HQ3kyk48Jnn-GfZIpfUkKTTbbAl
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, mean_squared_error
import numpy as np
import joblib

# Load the dataset
data = pd.read_csv("/content/exercise_dataset.csv")

# Check for missing values
if data.isnull().sum().sum() > 0:
    data = data.dropna()

# Check for duplicate values
data = data.drop_duplicates()

# Function to remove outliers
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Removing outliers from the relevant columns
columns_with_outliers = ['Calories Burn', 'Dream Weight', 'Actual Weight', 'Age', 'Duration', 'Heart Rate', 'BMI', 'Exercise Intensity']
for column in columns_with_outliers:
    data = remove_outliers(data, column)

# Feature selection (you may adjust this depending on your problem)
X = data[['Age', 'Duration', 'Heart Rate', 'BMI', 'Exercise Intensity']]
y = data['Calories Burn']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Save the trained model
joblib.dump(model, 'linear_regression_model.pkl')

print(f"Model saved with RMSE: {rmse}")

from google.colab import files

# Assuming you have saved the model as 'linear_regression_model.pkl'
files.download('linear_regression_model.pkl')