import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and target
X = data.drop("disease", axis=1)
y = data["disease"]

# Train model directly
model = DecisionTreeClassifier()
model.fit(X, y)

# Title
st.title("🩺 AI Medical Diagnosis System")

st.write("Select Symptoms")

# Convert Yes/No
def convert_input(value):
    return 1 if value == "Yes" else 0

# Inputs
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

# Prediction
if st.button("Predict Disease"):

    symptoms = pd.DataFrame(
        [[fever, cough, headache, fatigue]],
        columns=["fever", "cough", "headache", "fatigue"]
    )

    prediction = model.predict(symptoms)

    st.success(f"Predicted Disease: {prediction[0]}")

    st.info("Prediction generated using AI and Machine Learning")