from fastapi import FastAPI
from app.routes import fraud   # or wherever fraud.py is

app = FastAPI()

app.include_router(fraud.router, prefix="/fraud", tags=["Fraud"])