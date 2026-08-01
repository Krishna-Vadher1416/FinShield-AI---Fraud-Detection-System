from pydantic import BaseModel

class Transaction(BaseModel):
    user_id: int
    amount: float
    location: str
    timestamp: str
    merchant: str