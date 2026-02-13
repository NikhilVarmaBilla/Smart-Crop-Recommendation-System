import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

print("Smart Crop Recommendation System")

print("--------------------------------")
N = float(input("Enter Nitrogen (N): "))
P = float(input("Enter Phosphorus (P): "))
K = float(input("Enter Potassium (K): "))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
ph = float(input("Enter pH value: "))
rainfall = float(input("Enter Rainfall: "))

sample = pd.DataFrame(
    [[N, P, K, temperature, humidity, ph, rainfall]],
    columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
)

prediction = model.predict(sample)

print("\nRecommended Crop:", prediction[0])
