import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("heartdiseaseprediction.pkl")

st.title("Heart Disease Prediction App")
st.write("Enter the patient details to predict the presence of heart disease.")

# Input features
age = st.number_input("Age", min_value=0, max_value=120, value=50)
gender = st.selectbox("Gender", ["Male", "Female"])
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=400, value=200)
blood_pressure = st.number_input("Blood Pressure", min_value=60, max_value=200, value=120)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=70)
smoking = st.selectbox("Smoking", ["Current", "Never"])
alcohol = st.selectbox("Alcohol Intake", ["None", "Moderate", "Heavy"])
exercise_hours = st.slider("Exercise Hours per Week", 0, 20, 3)
family_history = st.selectbox("Family History of Heart Disease", ["Yes", "No"])
diabetes = st.selectbox("Diabetes", ["Yes", "No"])
obesity = st.selectbox("Obesity", ["Yes", "No"])
stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
blood_sugar = st.number_input("Blood Sugar", min_value=50, max_value=300, value=100)
exercise_angina = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
chest_pain_type = st.selectbox("Chest Pain Type", [
    "Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"
])

# Convert inputs to numerical format
gender_val = 1 if gender == "Male" else 0
smoking_val = 1 if smoking == "Current" else 0
alcohol_val = {"None": 0, "Moderate": 1, "Heavy": 2}[alcohol]
family_val = 1 if family_history == "Yes" else 0
diabetes_val = 1 if diabetes == "Yes" else 0
obesity_val = 1 if obesity == "Yes" else 0
angina_val = 1 if exercise_angina == "Yes" else 0
chest_pain_val = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}[chest_pain_type]

# Prepare feature array
features = np.array([[
    age, gender_val, cholesterol, blood_pressure, heart_rate,
    smoking_val, alcohol_val, exercise_hours, family_val,
    diabetes_val, obesity_val, stress_level, blood_sugar,
    angina_val, chest_pain_val
]])

# Predict
if st.button("Predict"):
    prediction = model.predict(features)[0]
    result = "🔴 At Risk of Heart Disease" if prediction == 1 else "🟢 No Heart Disease Detected"
    st.subheader(f"Prediction: {result}")
