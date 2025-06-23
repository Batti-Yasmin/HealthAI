from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.ibm_granite import ask_ibm_granite

router = APIRouter()

class TreatmentRequest(BaseModel):
    condition: str
    age: int
    gender: str
    existing_conditions: str = ""

@router.post("/treatment")
def generate_treatment(data: TreatmentRequest):
    prompt = (
        f"A {data.age}-year-old {data.gender} patient with the condition '{data.condition}'. "
        f"Existing conditions: {data.existing_conditions}. "
        f"Provide a personalized treatment plan including medications, lifestyle changes, and follow-up care."
    )
    response = ask_ibm_granite(prompt)
    return {"treatment_plan": response}
