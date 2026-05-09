import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and target
X = data.drop("disease", axis=1)
y = data["disease"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# App title
st.title("🩺 AI Medical Diagnosis System")

st.write("Select Symptoms")

# Convert Yes/No to 1/0
def convert_input(value):
    return 1 if value == "Yes" else 0

# User inputs
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

# Prediction button
if st.button("Predict Disease"):

    symptoms = pd.DataFrame(
        [[fever, cough, headache, fatigue]],
        columns=["fever", "cough", "headache", "fatigue"]
    )

    prediction = model.predict(symptoms)

    st.success(f"Predicted Disease: {prediction[0]}")

    disease = prediction[0]

    # Doctor recommendation

    if disease == "Flu":
        st.warning("Recommended Doctor: General Physician")

    elif disease == "Dengue":
        st.warning("Recommended Doctor: Medicine Specialist")

    elif disease == "Cold":
        st.warning("Recommended Doctor: ENT Specialist")

    elif disease == "Migraine":
        st.warning("Recommended Doctor: Neurologist")

    elif disease == "Malaria":
        st.warning("Recommended Doctor: Infectious Disease Specialist")

    elif disease == "Sinusitis":
        st.warning("Recommended Doctor: ENT Specialist")

    elif disease == "No Disease":
        st.success("No doctor needed. You seem healthy.")

    st.info("Prediction generated using AI and Machine Learning")