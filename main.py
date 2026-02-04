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

    # Validate API key
    if x_api_key != "test123":
        raise HTTPException(status_code=401, detail="Invalid API key")

    # Validate request payload
    if not data.audio_base64 and not data.audio_url:
        raise HTTPException(status_code=400, detail="No audio provided. Send audio_base64 or audio_url.")
        
    # Replace this with your real AI model if available
    classification_result = "AI-generated"
    confidence_score = 0.92

    # Return proper JSON response
    return {
        "classification": classification_result,
        "confidence": confidence_score,
        "status": "success"
    }

# Optional: handle unexpected errors globally
@app.exception_handler(Exception)
def global_exception_handler(request, exc):
    return {
        "status": "error",
        "message": str(exc)
    }
