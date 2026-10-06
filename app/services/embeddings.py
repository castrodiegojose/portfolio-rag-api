from sentence_transformers import SentenceTransformer
from app.core.config import settings

model=SentenceTransformer(settings.embedding_model)

def embed_texts(texts: list[str]):
    return model.encode(texts)
    