import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("Obesitymodel.pkl", "rb") as file:
    model = pickle.load(file)

# Mapping obesity class to label
obesity_labels = {
    0: 'Normal Weight',
    1: 'Overweight Level I',
    2: 'Overweight Level II',
    3: 'Obesity Type I',
    4: 'Obesity Type II',
    5: 'Obesity Type III',
    6: 'Insufficient Weight'
}

# App title
st.title("Obesity Level Prediction App")

st.markdown("### Fill in your details to get your obesity level prediction.")

# Input fields
def user_input_features():
    Gender = st.selectbox("Gender", ['Female', 'Male'])  # Female=0, Male=1
    Age = st.slider("Age", 10, 100, 25)
    Height = st.slider("Height (meters)", 1.3, 2.2, 1.7)
    Weight = st.slider("Weight (kg)", 30, 200, 70)
    family_history = st.selectbox("Family History of Overweight", ['no', 'yes'])  # no=0, yes=1
    FCVC = st.slider("Frequency of Vegetable Consumption (1-3)", 1.0, 3.0, 2.0)
    NCP = st.slider("Number of Meals per Day", 1.0, 4.0, 3.0)
    SMOKE = st.selectbox("Do You Smoke?", ['no', 'yes'])  # no=0, yes=1
    CH2O = st.slider("Daily Water Intake (liters)", 1.0, 3.0, 2.0)
    FAF = st.slider("Physical Activity Frequency (hrs/week)", 0.0, 5.0, 1.0)
    TUE = st.slider("Technology Use (hrs/day)", 0.0, 5.0, 2.0)
    MTRANS = st.selectbox("Primary Transport Mode", ['Public_Transportation', 'Automobile', 'Motorbike', 'Bike', 'Walking'])  # Walking=1, others=0

    # Encode categorical features based on your preprocessing
    Gender = 1 if Gender == 'Male' else 0
    family_history = 1 if family_history == 'yes' else 0
    SMOKE = 1 if SMOKE == 'yes' else 0
    MTRANS = 1 if MTRANS == 'Walking' else 0

    # Feature array
    features = np.array([[Gender, Age, Height, Weight, family_history, FCVC, NCP,
                          SMOKE, CH2O, FAF, TUE, MTRANS]])
    return features

# Get user input
input_data = user_input_features()

# Predict button
if st.button("Predict Obesity Level"):
    prediction = model.predict(input_data)
    label = obesity_labels.get(prediction[0], "Unknown")
    st.success(f"Predicted Obesity Category: **{label}**")
