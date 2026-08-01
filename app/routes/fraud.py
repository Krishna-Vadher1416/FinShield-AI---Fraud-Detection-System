from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import os

# ✅ Import Gemini function
from app.services.llm_explainer import explain_fraud

router = APIRouter()

# ✅ Safe model loading
try:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    model_path = os.path.join(BASE_DIR, "ml", "fraud_model.pkl")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    model = joblib.load(model_path)
    print("✅ ML model loaded successfully")

except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None


# ✅ Request schema
class Transaction(BaseModel):
    user_id: int
    amount: float
    location: str
    merchant: str
    timestamp: str


# ✅ Health check
@router.get("/health")
def health_check():
    return {"status": "ok"}


# ✅ Main fraud check API
@router.post("/check")
def check_fraud(txn: Transaction):

    if model is None:
        raise HTTPException(status_code=500, detail="ML model not loaded")

    try:
        # ✅ Feature engineering
        location_flag = 1 if txn.location.lower() != "india" else 0
        merchant_flag = 1 if txn.merchant.lower() in ["unknown", "suspicious"] else 0

        features = [[txn.amount, location_flag, merchant_flag]]

        # ✅ ML prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        # ✅ Convert to readable result
        result_text = "Fraudulent" if prediction == 1 else "Safe"

        # ✅ Gemini AI explanation
        ai_explanation = explain_fraud(txn, result_text)

        # ✅ Reasons (cleaned list)
        reasons = [
            "High amount" if txn.amount > 50000 else None,
            "Foreign location" if location_flag else None,
            "Suspicious merchant" if merchant_flag else None
        ]
        reasons = [r for r in reasons if r]  # remove None

        return {
            "is_fraud": bool(prediction),
            "risk_score": round(float(probability), 2),
            "reasons": reasons,
            "ai_explanation": ai_explanation
        }

    except Exception as e:
        print(f"❌ Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))