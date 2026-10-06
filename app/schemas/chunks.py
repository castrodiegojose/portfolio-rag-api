from pydantic import BaseModel

class ChunksResponse(BaseModel):
    id: str
    source: str
    section: str
    text:str