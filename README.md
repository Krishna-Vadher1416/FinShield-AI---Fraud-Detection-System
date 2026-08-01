🛡️ FinShield AI – Fraud Detection System

FinShield AI is an intelligent fraud detection system that leverages Machine Learning and LLM-based explanations to identify and explain potentially fraudulent financial transactions. It provides a backend API, a frontend interface, and a trained ML model for real-time predictions.

🚀 Project Overview

This project is designed to:

Detect fraudulent transactions using a trained ML model
Provide human-readable explanations using LLM
Offer an API for integration with other systems
Deliver a simple frontend interface for user interaction
🧠 Key Features
🔍 Fraud Detection Model
Uses a trained ML model (fraud_model.pkl) to classify transactions.
🤖 LLM-Based Explanation
Explains why a transaction is marked as fraud or safe.
⚡ FastAPI Backend
High-performance API for prediction and explanation.
🎯 Modular Architecture
Clean separation of routes, services, models, and database.
💻 Frontend UI
Simple interface to test fraud detection.
📁 Project Structure
FinShield-AI/
│
├── app/
│   ├── db/
│   │   └── database.py          # Database connection
│   ├── models/
│   │   └── schemas.py           # Request/response schemas
│   ├── routes/
│   │   └── fraud.py             # API routes
│   ├── services/
│   │   ├── detection.py         # Fraud detection logic
│   │   └── llm_explainer.py     # Explanation generation
│   └── main.py                  # FastAPI entry point
│
├── frontend/
│   └── app.py                   # Frontend interface
│
├── ml/
│   ├── fraud_model.pkl          # Trained ML model
│   └── train_model.py           # Model training script
│
├── screenshots/                 # Project screenshots & docs
│
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
└── .gitignore
⚙️ Technologies Used
Python
FastAPI
Scikit-learn
Pandas & NumPy
Pickle (Model Serialization)
Streamlit / Frontend Python App
LLM Integration (for explanations)
🔄 How It Works
User inputs transaction details
Backend API processes the data
ML model predicts fraud or not
LLM generates explanation
Result is returned to frontend
📊 API Endpoints
🔹 Fraud Detection
POST /predict

Request Example:

{
  "amount": 1000,
  "transaction_type": "transfer",
  "oldbalanceOrg": 5000,
  "newbalanceOrig": 4000
}

Response Example:

{
  "fraud": true,
  "confidence": 0.92,
  "explanation": "This transaction is flagged due to unusual amount and balance mismatch."
}
🤖 Machine Learning Model
Trained using historical transaction data
Stored as: ml/fraud_model.pkl
Training script: ml/train_model.py
🧩 Core Modules Explained
📌 detection.py

Handles:

Model loading
Prediction logic
📌 llm_explainer.py

Handles:

Converting predictions into human explanations
📌 fraud.py

Handles:

API routing
Request/response handling
🖥️ Frontend
Located in frontend/app.py
Allows users to:
Input transaction data
View prediction results
See explanations
📌 Use Cases
Banking fraud detection
Payment gateway monitoring
Financial risk analysis
Real-time transaction validation
📷 Screenshots

Available in the screenshots/ folder:

Swagger UI
Project demos
Final reports
📈 Future Improvements
Real-time streaming data support
Advanced deep learning models
Dashboard analytics
Deployment on cloud (AWS/GCP)
User authentication system
👨‍💻 Author

Krishna Vadher

⭐ Conclusion

FinShield AI combines Machine Learning + AI Explainability to build a practical fraud detection system that is not only accurate but also interpretable.
