from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.ibm_granite import ask_ibm_granite

router = APIRouter()

class RemedyRequest(BaseModel):
    condition: str

@router.post("/remedies")
def get_remedies(data: RemedyRequest):
    prompt = f"Suggest safe and effective home remedies for: {data.condition}. Include natural treatments, herbal options, and safety precautions if any."
    response = ask_ibm_granite(prompt)
    return {"remedies": response}
