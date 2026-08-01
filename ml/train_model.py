import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Generate dummy dataset
np.random.seed(42)

data_size = 1000

data = pd.DataFrame({
    "amount": np.random.randint(100, 100000, data_size),
    "location": np.random.randint(0, 2, data_size),  # 0 = local, 1 = foreign
    "merchant": np.random.randint(0, 2, data_size),  # 0 = normal, 1 = suspicious
    "is_fraud": np.random.randint(0, 2, data_size)
})

X = data[["amount", "location", "merchant"]]
y = data["is_fraud"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "ml/fraud_model.pkl")

print("✅ Model trained and saved!")