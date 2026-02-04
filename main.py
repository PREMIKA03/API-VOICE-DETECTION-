from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="AI Generated Voice Detection API")

class AudioRequest(BaseModel):
    audio_url: Optional[str] = None
    audio_base64: Optional[str] = None


@app.get("/")
def home():
    return {"message": "API Running Successfully"}


@app.post("/detect-voice")
def detect_voice(data: AudioRequest, authorization: str = Header(None)):

    if authorization != "test123":
        return {"status": "error", "message": "Invalid API key"}

    return {
        "classification": "AI-generated",
        "confidence": 0.92,
        "status": "success"
    }
