# Streamlit App for Life Expectancy Prediction using KNN Model

import streamlit as st
import pickle
import pandas as pd

# Title
st.title("Life Expectancy Prediction App")
st.markdown("Enter the following details to predict life expectancy:")

# Load the saved model
with open('knn_life_expectancy_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to take user inputs
def user_inputs():
    adult_mortality = st.number_input('Adult Mortality', min_value=0, max_value=1000, value=150)
    infant_deaths = st.number_input('Infant Deaths', min_value=0, max_value=1000, value=5)
    alcohol = st.number_input('Alcohol Consumption (litres per capita)', min_value=0.0, max_value=20.0, value=5.0)
    percentage_expenditure = st.number_input('Percentage Expenditure', min_value=0, max_value=100000, value=100)
    hepatitis_b = st.number_input('Hepatitis B (%)', min_value=0, max_value=100, value=90)
    measles = st.number_input('Measles Cases', min_value=0, max_value=100000, value=10)
    bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, value=20.0)
    under_five_deaths = st.number_input('Under-Five Deaths', min_value=0, max_value=1000, value=5)
    polio = st.number_input('Polio (%)', min_value=0, max_value=100, value=90)
    total_expenditure = st.number_input('Total Expenditure (% of GDP)', min_value=0.0, max_value=100.0, value=5.0)

    inputs = {
        'Adult Mortality': adult_mortality,
        'infant deaths': infant_deaths,
        'Alcohol': alcohol,
        'percentage expenditure': percentage_expenditure,
        'Hepatitis B': hepatitis_b,
        'Measles': measles,
        'BMI': bmi,
        'under-five deaths': under_five_deaths,
        'Polio': polio,
        'Total expenditure': total_expenditure
    }

    return pd.DataFrame([inputs])

# Capture input features
input_df = user_inputs()

# Predict button
if st.button('Predict Life Expectancy'):
    prediction = model.predict(input_df)
    st.success(f'Predicted Life Expectancy: {prediction[0]:.2f} years')