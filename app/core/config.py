from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    allowed_origins: list[str]
    documents_dir: Path
    embedding_model: str
    chroma_path: Path
    chroma_collection: str
    ollama_host: str
    ollama_model: str
    enable_debug_routers: bool = False
    retrieve_k: int = 5
    retrieve_max_distance: float = 1.05

try:
    settings = Settings()
except Exception as e:
    raise RuntimeError(
        "Invalid configuration. Copy .env.example to .env and fill the values."
    ) from e