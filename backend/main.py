from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import analyze_message

app = FastAPI()


class MessageRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Welcome to SmartPay Guard API"}


@app.post("/analyze")
def analyze(request: MessageRequest):
    risk_score, risk_level, reasons = analyze_message(request.message)

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons
    }