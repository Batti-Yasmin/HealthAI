from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.ibm_granite import ask_ibm_granite

router = APIRouter()

class PredictRequest(BaseModel):
    symptoms: str

@router.post("/predict")
def predict_disease(data: PredictRequest):
    prompt = f"The patient reports these symptoms: {data.symptoms}. What are the most likely medical conditions? Respond with top 3 possibilities, likelihood (high/medium/low), and recommended next steps."
    response = ask_ibm_granite(prompt)
    return {"prediction": response}
