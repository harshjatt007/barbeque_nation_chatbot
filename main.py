from fastapi import FastAPI
from app.routes import chatbot

app = FastAPI()

app.include_router(chatbot.router, prefix="/api/chatbot", tags=["Chatbot"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Barbeque Nation Chatbot API"}