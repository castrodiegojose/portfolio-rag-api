from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from app.core.config import settings
from app.routers import chat, corpus

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins= settings.allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

@app.get("/")
def playground():
    return FileResponse(STATIC_DIR / "chat.html")


@app.get("/health")
def health():
    return {"ok":True}

app.include_router(chat.router)

if settings.enable_debug_routers:
    app.include_router(corpus.router)
