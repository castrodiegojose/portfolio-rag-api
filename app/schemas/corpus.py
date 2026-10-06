from pydantic import BaseModel

class File(BaseModel):
    name:str
    suffix:str
    size: int

class CorpusResponse(BaseModel):
    directory: str
    files: list[File]