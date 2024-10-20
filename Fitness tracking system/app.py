import streamlit as st
import joblib
import numpy as np

# Load the trained model from the .pkl file
model = joblib.load('linear_regression_model.pkl')

# Streamlit app
st.title("Fitness calorie checker")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=25)
duration = st.number_input("Duration (minutes)", min_value=1, max_value=300, value=30)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=70)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
exercise_intensity = st.slider("Exercise Intensity", min_value=1, max_value=10, value=5)

# Prediction button
if st.button("Predict Calories Burned"):
    features = np.array([[age, duration, heart_rate, bmi, exercise_intensity]])
    prediction = model.predict(features)
    st.write(f"Estimated Calories Burned: {prediction[0]:.2f} calories")
