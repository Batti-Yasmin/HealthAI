from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.ai.ibm_granite import ask_ibm_granite

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat_response(request: ChatRequest):
    prompt = f"The patient asks: {request.message}\nProvide a helpful, empathetic medical response."
    response = ask_ibm_granite(prompt)
    return {"response": response}
