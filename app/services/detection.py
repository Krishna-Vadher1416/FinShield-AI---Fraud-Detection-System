def detect_fraud(transaction):
    score = 0
    reasons = []

    if transaction.amount > 10000:
        score += 0.4
        reasons.append("High transaction amount")

    if transaction.location not in ["India"]:
        score += 0.3
        reasons.append("Unusual location")

    if transaction.merchant.lower() in ["unknown", "suspicious"]:
        score += 0.3
        reasons.append("Suspicious merchant")

    is_fraud = score > 0.5

    return {
        "is_fraud": is_fraud,
        "risk_score": score,
        "reasons": reasons
    }