from app.core.config import settings
from pathlib import Path
from slugify import slugify #Biblioteca para sacar acentos!
from langchain_text_splitters import MarkdownHeaderTextSplitter
from .embeddings import embed_texts
from .store import save_items

def list_chunks(file_name: str | None = None):
    if file_name:
        name = file_name.strip()
        if not name.endswith(".md") or "/" in name or "\\" in name or name.startswith("."):
            raise ValueError(f"Invalid document name: {name!r}")
        documents_dir = settings.documents_dir.resolve()
        candidate = (documents_dir / name).resolve()
        if not candidate.is_relative_to(documents_dir):
            raise ValueError(f"Invalid document name: {name!r}")
        if not candidate.is_file():
            raise FileNotFoundError(f"Document not found: {name}")
        return chunking_process(candidate)
    else:
        #traer todos los archivos 
        documents_dir= Path(settings.documents_dir)
        if not documents_dir.is_dir():
            raise FileNotFoundError(f"Documents directory is missing: {documents_dir}")
        
        files=[]
        for doc in documents_dir.iterdir():
            if not doc.is_file():
                continue
            if doc.name.startswith(".") or doc.suffix.lower() != ".md":
                continue
            files.extend(chunking_process(doc))
        return files


def chunking_process(doc_path: Path):
    text=doc_path.read_text(encoding="utf-8")
    headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    md_header_splits = markdown_splitter.split_text(text)

    arr=[]
    for p in md_header_splits:    
        body = p.page_content.replace("\n", " ")
        section = p.metadata.get("Header 2") or p.metadata.get("Header 1") or "body"
        slug = slugify(section)
        arr.append({
            "id": f"{doc_path.name}#{slug}",
            "source": doc_path.name,
            "section": section,
            "text": body,
        })

    return arr

def run_pipeline():
    chunks = list_chunks()
    to_embed = [f"{c['source']} {c['section']}. {c['text']}" for c in chunks]
    vectors = embed_texts(to_embed)
    if len(chunks) != vectors.shape[0]:
        raise ValueError(f"chunks and vectors length mismatch: {len(chunks)} != {vectors.shape[0]}")
    collection_name = save_items(chunks, vectors)
    return len(chunks), collection_name
