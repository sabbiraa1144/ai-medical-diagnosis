import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and target
X = data.drop("disease", axis=1)
y = data["disease"]

# Train model with all data
model = DecisionTreeClassifier()

model.fit(X, y)

# Accuracy manually
accuracy = model.score(X, y)

print("Model Accuracy:", accuracy * 100, "%")

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully!")