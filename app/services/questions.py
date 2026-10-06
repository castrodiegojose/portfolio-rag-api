from app.services.store import query_items
from app.core.config import settings
from .embeddings import embed_texts

def ask_question(question):
    embbeding_question = embed_texts([question])
    raw = query_items(embbeding_question[0].tolist(), settings.retrieve_k)
    hits = []
    for i in range(len(raw["ids"][0])):
        hits.append({
            "id": raw["ids"][0][i],
            "text": raw["documents"][0][i],
            "source": raw["metadatas"][0][i]["source"],
            "section": raw["metadatas"][0][i]["section"],
            "distance": raw["distances"][0][i],
        })
    hits = [h for h in hits if h["distance"] <= settings.retrieve_max_distance]
    citations = [
        {
            "id": h['id'],
            "source": h["source"],
            "section": h["section"]
        }
        for h in hits
    ]
    return hits, citations