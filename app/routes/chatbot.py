from fastapi import APIRouter, Request
from app.services.chat_service import get_response

router = APIRouter()

@router.post("/message")
async def chat_with_bot(request: Request):
    body = await request.json()
    user_message = body.get("message", "")
    response = get_response(user_message)
    return {"response": response}