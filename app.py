import streamlit as st
import joblib
import pandas as pd
from PIL import Image

# Set up the page
st.set_page_config(page_title="Life Expectancy Predictor", page_icon="🌍", layout="centered")

# Title and description
st.title("🌍 Life Expectancy Prediction App")
st.markdown("### Enter the following details to predict life expectancy:")

# Load the saved model safely using joblib
try:
    model = joblib.load('knn_life_expectancy_model.pkl')
except FileNotFoundError:
    st.error("❌ Model file not found. Please upload 'knn_life_expectancy_model.pkl' in the same directory.")
    st.stop()

# Sidebar for user inputs
st.sidebar.header("Input Parameters")

def user_inputs():
    adult_mortality = st.sidebar.number_input('Adult Mortality', min_value=0, max_value=1000, value=150)
    infant_deaths = st.sidebar.number_input('Infant Deaths', min_value=0, max_value=1000, value=5)
    alcohol = st.sidebar.number_input('Alcohol Consumption (litres per capita)', min_value=0.0, max_value=20.0, value=5.0)
    percentage_expenditure = st.sidebar.number_input('Percentage Expenditure', min_value=0, max_value=100000, value=100)
    hepatitis_b = st.sidebar.number_input('Hepatitis B (%)', min_value=0, max_value=100, value=90)
    measles = st.sidebar.number_input('Measles Cases', min_value=0, max_value=100000, value=10)
    bmi = st.sidebar.number_input('BMI', min_value=0.0, max_value=100.0, value=20.0)
    under_five_deaths = st.sidebar.number_input('Under-Five Deaths', min_value=0, max_value=1000, value=5)
    polio = st.sidebar.number_input('Polio (%)', min_value=0, max_value=100, value=90)
    total_expenditure = st.sidebar.number_input('Total Expenditure (% of GDP)', min_value=0.0, max_value=100.0, value=5.0)

    data = {
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

    return pd.DataFrame([data])

input_df = user_inputs()

# Display input summary
st.subheader("Your Input Summary:")
st.write(input_df)

# Predict button
if st.button('🎯 Predict Life Expectancy'):
    prediction = model.predict(input_df)
    st.success(f"✅ Predicted Life Expectancy: **{prediction[0]:.2f} years**")
