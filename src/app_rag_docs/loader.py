# src/app_rag_docs/loader.py

from pathlib import Path

# This assumes this file lives in: <repo_root>/src/app_rag_docs/loader.py
# parents[0] = app_rag_docs, [1] = src, [2] = repo root
DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "rag_docs"


def load_documents():
    """
    Load all .md files from data/rag_docs/.
    Returns a list of {"path": Path, "text": str}.
    """
    docs = []
    for file in DATA_DIR.glob("*.md"):
        text = file.read_text(encoding="utf-8")
        docs.append({"path": file, "text": text})
    return docs


def chunk_text(text: str, max_chars: int = 800, overlap: int = 200):
    """
    Simple character-based chunking with overlap.
    This is good enough for Week 4.
    """
    chunks = []
    start = 0
    n = len(text)

    while start < n:
        end = min(start + max_chars, n)
        chunk = text[start:end]
        chunks.append(chunk)
        # move forward with overlap
        if end == n:
            break
        start = max(end - overlap, 0)

    return chunks


def load_and_chunk_all():
    """
    Load all docs and return a list of chunk dicts:
    {
        "doc_name": str,
        "chunk_index": int,
        "text": str
    }
    """
    docs = load_documents()
    all_chunks = []

    for doc in docs:
        chunks = chunk_text(doc["text"])
        for idx, chunk in enumerate(chunks):
            all_chunks.append(
                {
                    "doc_name": doc["path"].name,
                    "chunk_index": idx,
                    "text": chunk,
                }
            )

    return all_chunks

