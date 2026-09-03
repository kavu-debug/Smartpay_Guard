from fastapi import FastAPI, UploadFile, File, HTTPException
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


@app.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...)):

    # Allow only text files for now
    if not file.filename or not file.filename.lower().endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Only .txt files are supported."
        )

    try:
        content = await file.read()
        message = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="The file must be a valid UTF-8 text file."
        )

    risk_score, risk_level, reasons = analyze_message(message)

    return {
        "filename": file.filename,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons
    }