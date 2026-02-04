from fastapi import FastAPI, Header, Form, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="AI Generated Voice Detection API")

class AudioRequest(BaseModel):
    audio_url: Optional[str] = None
    audio_base64: Optional[str] = None

@app.get("/")
def home():
    return {
        "message": "API is live! Use POST /detect-voice to classify audio.",
        "example_endpoint": "/detect-voice"
    }

# Accept JSON OR form-data
@app.post("/detect-voice")
def detect_voice(
    audio_base64: Optional[str] = Form(None),
    audio_url: Optional[str] = Form(None),
    x_api_key: str = Header(None)
):
    # Validate API key
    if x_api_key != "test123":
        raise HTTPException(status_code=401, detail="Invalid API key")

    # Validate that audio is provided
    if not audio_base64 and not audio_url:
        raise HTTPException(status_code=400, detail="No audio provided. Send audio_base64 or audio_url.")

    # Dummy AI classification
    classification_result = "AI-generated"
    confidence_score = 0.92

    return {
        "classification": classification_result,
        "confidence": confidence_score,
        "status": "success"
    }
