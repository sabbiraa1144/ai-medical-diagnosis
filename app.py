import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🩺 AI Medical Diagnosis System")

st.write("Select Symptoms")

# Convert Yes/No to 1/0
def convert_input(value):
    if value == "Yes":
        return 1
    return 0

# User input
fever = convert_input(
    st.selectbox("Fever", ["No", "Yes"])
)

cough = convert_input(
    st.selectbox("Cough", ["No", "Yes"])
)

headache = convert_input(
    st.selectbox("Headache", ["No", "Yes"])
)

fatigue = convert_input(
    st.selectbox("Fatigue", ["No", "Yes"])
)

# Predict
if st.button("Predict Disease"):

    symptoms = pd.DataFrame(
        [[fever, cough, headache, fatigue]],
        columns=["fever", "cough", "headache", "fatigue"]
    )

    prediction = model.predict(symptoms)

    st.success(f"Predicted Disease: {prediction[0]}")

    st.info("Prediction generated using AI and Machine Learning")