from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

# =========================
# Chargement du modèle
# =========================

model = joblib.load("stacking_svm_lr_nb.pkl")

# =========================
# Initialisation API
# =========================

app = FastAPI()

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Structure requête
# =========================

class CommentRequest(BaseModel):
    text: str

# =========================
# Route test
# =========================

@app.get("/")
def home():
    return {"message": "Darija Sentiment API is running"}

# =========================
# Prediction
# =========================

@app.post("/predict")
def predict_sentiment(request: CommentRequest):

    prediction = model.predict([request.text])[0]

    probabilities = model.predict_proba([request.text])[0]

    return {
        "text": request.text,
        "prediction": prediction,
        "probabilities": {
            "negatif": float(probabilities[0]),
            "neutre": float(probabilities[1]),
            "positif": float(probabilities[2])
        }
    }