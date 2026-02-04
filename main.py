from fastapi import FastAPI, Header, Form, HTTPException

app = FastAPI(title="AI Generated Voice Detection API")

# Friendly home route
@app.get("/")
def home():
    return {
        "message": "API is live! Use POST /detect-voice to classify audio.",
        "example_endpoint": "/detect-voice"
    }

# Main POST endpoint
@app.post("/detect-voice")
def detect_voice(
    audio_base64: str = Form(None),
    audio_url: str = Form(None),
    x_api_key: str = Header(None)
):
    # 1️⃣ Validate API key
    if x_api_key != "test123":
        raise HTTPException(status_code=401, detail="Invalid API key")

    # 2️⃣ Validate that audio is provided
    if not audio_base64 and not audio_url:
        raise HTTPException(status_code=400, detail="No audio provided. Send audio_base64 or audio_url.")

    # 3️⃣ Dummy AI detection (replace with real logic if needed)
    classification_result = "AI-generated"
    confidence_score = 0.92

    # 4️⃣ Return structured JSON
    return {
        "classification": classification_result,
        "confidence": confidence_score,
        "status": "success"
    }
