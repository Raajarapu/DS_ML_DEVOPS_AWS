from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="Fraud Detection API",
    description="ML inference API for fraud detection",
    version="1.0.0"
)

model = joblib.load("fraud_model.pkl")


class Transaction(BaseModel):
    amount: float
    hour: int
    num_tx_past_day: int


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "fraud-detection-api"
    }


@app.post("/predict")
def predict(transaction: Transaction):

    features = pd.DataFrame([{
        "amount": transaction.amount,
        "hour": transaction.hour,
        "num_tx_past_day": transaction.num_tx_past_day
    }])

    prediction = int(model.predict(features)[0])
    probability = float(model.predict_proba(features)[0][1])

    return {
        "is_fraud": prediction,
        "fraud_probability": round(probability, 4)
    }
