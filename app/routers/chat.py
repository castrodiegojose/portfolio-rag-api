from fastapi import APIRouter, HTTPException
from app.schemas.chat_request import ChatRequest, ChatResponse
from app.services.generate import generate_reply
from app.services.questions import ask_question

router=APIRouter()

@router.post("/chat")
def chat(request:ChatRequest) -> ChatResponse:
    try:
        session_id = request.sessionId
        hits, citations = ask_question(request.message)
        reply = generate_reply(request.message, hits, request.locale)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Index not found. Run ingest first.")
    except ConnectionError:
        raise HTTPException(status_code=503, detail="Language model is unavailable.")
    except Exception:
        raise HTTPException(status_code=500, detail="Chat failed.")

    return ChatResponse(
        reply=reply,
        citations=citations,
        sessionId=session_id
    )
