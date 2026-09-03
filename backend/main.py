from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.analyzer import analyze_message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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