import os
import time
from dotenv import load_dotenv
from google import genai

# Load env
load_dotenv()

# Initialize client (NEW SDK way)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def explain_fraud(transaction, result):
    try:
        start = time.time()

        prompt = f"""
You are a fraud detection expert.

Transaction Details:
- Amount: {transaction.amount}
- Location: {transaction.location}
- Merchant: {transaction.merchant}

Prediction Result: {result}

Give a VERY SHORT explanation (max 2 lines).
Be clear and direct.
"""

        # Generate response (FAST model)
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        

        # Safe extraction
        if response and response.text:
            return response.text.strip()

        return "No explanation generated"

    except Exception as e:
        print("Gemini Error:", e)
        return "AI explanation unavailable"