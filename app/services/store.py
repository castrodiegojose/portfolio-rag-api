import chromadb
from app.core.config import settings
from chromadb.errors import NotFoundError

client= chromadb.PersistentClient(path=str(settings.chroma_path))

def save_items(items, vector):
    try:
        client.delete_collection(settings.chroma_collection)
    except NotFoundError:
        pass
    collection = client.get_or_create_collection(name=settings.chroma_collection)
    collection.add(
        ids=[c["id"] for c in items],
        documents=[c["text"] for c in items],
        embeddings= vector.tolist(),
        metadatas=[{"source": c["source"], "section":c["section"]} for c in items]
    )
    

    return collection.name

def query_items(query_vector, k: int = 5):
    try:
        collection = client.get_collection(name=settings.chroma_collection)
    except NotFoundError:
        raise FileNotFoundError(
            f"Collection {settings.chroma_collection!r} not found. Run ingest first."
        ) from None
    raw = collection.query(
        query_embeddings= [query_vector],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    return raw

