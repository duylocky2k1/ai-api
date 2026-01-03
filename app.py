import os
from fastapi import FastAPI
from pydantic import BaseModel

# ko hardcode tene app, override theo environment variable
APP_NAME = os.getenv("APP_NAME", "Mock AI API")

# init app (no load model + connect DB)
app = FastAPI(title=APP_NAME)

# Dùng pydantic để validate request + response
class Request(BaseModel):
    text: str

class Response(BaseModel):
    response: str

#Mock AI = stateless (easy scale + no mem leak issue)
@app.post("/predict", response_model=Response)
def predict(req: Request):
    return {
        "response": f"AI says: {req.text[::-1]}"
    }

# ✅ HEALTH ENDPOINT
@app.get("/health")
def health():
    return {"status": "ok"}