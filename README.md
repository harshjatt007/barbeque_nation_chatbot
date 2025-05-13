# Barbeque Nation Chatbot (Python Version)

This is a Python implementation of the Barbeque Nation conversational agent built using FastAPI.

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints

- `GET /` - Health check
- `POST /api/chatbot/message` - Send a message to the chatbot

## Environment Variables

Make sure to define the following in `.env`:
- `API_KEY`
- `BASE_URL`