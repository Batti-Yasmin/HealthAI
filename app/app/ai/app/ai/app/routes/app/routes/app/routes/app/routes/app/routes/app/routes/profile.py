from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Simulated in-memory profile (for demo)
patient_profile = {
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "conditions": "None",
    "allergies": "None"
}

class Profile(BaseModel):
    name: str
    age: int
    gender: str
    conditions: str
    allergies: str

@router.get("/profile")
def get_profile():
    return patient_profile

@router.post("/profile")
def update_profile(data: Profile):
    patient_profile.update(data.dict())
    return {"message": "Profile updated successfully", "profile": patient_profile}
