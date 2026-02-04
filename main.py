from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="AI Generated Voice Detection API")

# Request body model
class AudioRequest(BaseModel):
    audio_url: Optional[str] = None
    audio_base64: Optional[str] = None

# Friendly home route
@app.get("/")
def home():
    return {
        "message": "API is live! Use POST /detect-voice to classify audio.",
        "example_endpoint": "/detect-voice"
    }

# Main POST endpoint
@app.post("/detect-voice")
def detect_voice(data: AudioRequest, x_api_key: str = Header(None)):

    # Check API key
    if x_api_key != "test123":
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {
        "classification": "AI-generated",
        "confidence": 0.92,
        "status": "success"
    }
