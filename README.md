#  Heart Disease Prediction App

This is a simple web application built using *Streamlit* that predicts the likelihood of heart disease based on various health and lifestyle parameters. The backend model is an *SVM (Support Vector Machine)* classifier trained on a medical dataset.

## Project Overview

Heart disease remains one of the leading causes of death globally. Early detection through predictive modeling can help in timely intervention. This app allows users to input patient data and get instant predictions on the risk of heart disease.

## Features

Input fields for health and lifestyle parameters like:
  - Age, Gender, Cholesterol, Blood Pressure
  - Heart Rate, Smoking, Alcohol Intake
  - Diabetes, Obesity, Stress Level, etc.
- SVM model trained on labeled heart disease data
- Interactive and user-friendly UI using Streamlit
- Prediction output: *"At Risk"* or *"No Heart Disease"*

##  Model Used

Algorithm: Support Vector Machine (SVM)
Library: Scikit-learn
The model was trained on a structured dataset and saved using joblib for deployment.
Frontend: Streamlit
Backend: Python (SVM from Scikit-learn)
Libraries:
  - numpy
  - pandas
  - streamlit
  - joblib
  - scikit-learn
  - matplotlib
  - seaborn


