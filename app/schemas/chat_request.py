from pydantic import BaseModel
from enum import StrEnum

class Locale(StrEnum):
    EN="en"
    ES="es"

class ChatRequest(BaseModel):
    sessionId: str
    locale: Locale
    message: str

class Citation(BaseModel):
    id: str
    source: str
    section: str
class ChatResponse(BaseModel):
    reply: str
    citations: list[Citation]
    sessionId: str