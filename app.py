from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI(title="Fraud Detection API")

model = joblib.load("model/fraud_model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running"}

@app.post("/predict")
def predict(data: dict):
    print("Received data:", data)   # 👈 ADD THIS

    features = np.array(list(data.values())).reshape(1, -1)
    features[:, -1] = scaler.transform(features[:, -1].reshape(-1, 1)).flatten()

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    print("Prediction:", prediction, "Prob:", probability)  # 👈 ADD THIS

    return {
        "fraud_prediction": int(prediction),
        "fraud_probability": round(float(probability), 4)
    }

