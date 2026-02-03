from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.api.v1.chat_agent import router as chat_router

app = FastAPI(title="AI AGENTS", version="0.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api/v1", tags=["chat"])
