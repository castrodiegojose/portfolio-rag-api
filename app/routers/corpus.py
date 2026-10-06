from fastapi import APIRouter, HTTPException
from app.schemas.corpus import CorpusResponse
from app.schemas.chunks import ChunksResponse
from app.services.list_documents import list_documents
from app.services.chunking import list_chunks, run_pipeline
from app.services.questions import ask_question

router=APIRouter()

@router.get("/debug/corpus")
def get_path() -> CorpusResponse:
    try:
        list_docs = list_documents()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Files not found")
    return CorpusResponse(directory = list_docs["directory"], files= list_docs["files"])

@router.get("/debug/chunks")
def get_chunks(source: str | None = None) -> list[ChunksResponse]:
    try:
        list_chunk = list_chunks(source)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return list_chunk

@router.post("/debug/ingest")
def post_ingest():
    try:
        chunks, name_collection = run_pipeline()
    except Exception:
        raise HTTPException(status_code=500, detail="Ingest failed.")
    return {"chunks": chunks, "collection":name_collection}

@router.get("/debug/retrieve")
def get_retrieve(question: str):
    try:
        hits, citations = ask_question(question)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Index not found. Run ingest first.")
    except Exception:
        raise HTTPException(status_code=500, detail="Retrieve failed.")

    return {"hits": hits, "citations": citations}
