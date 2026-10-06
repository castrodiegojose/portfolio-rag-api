from pathlib import Path
from app.core.config import settings

def list_documents():
    documents_dir= Path(settings.documents_dir)
    if not documents_dir.is_dir():
        raise FileNotFoundError(f"Documents directory is missing: {documents_dir}")
    
    files=[]
    for doc in documents_dir.iterdir():
        if not doc.is_file():
            continue
        if doc.name.startswith(".") or doc.suffix.lower() != ".md":
            continue
        files.append(
            {
                "name": doc.name,
                "suffix": doc.suffix,
                "size": doc.stat().st_size
            }
        )
            
    files.sort(key=lambda f: f["name"])
    return {
        "directory":documents_dir.name,
        "files": files
    } 