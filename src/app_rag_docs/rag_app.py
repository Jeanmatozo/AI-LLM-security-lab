# src/app_rag_docs/rag_app.py
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from openai import OpenAI

from .loader import load_and_chunk_all
from .vectorstore import SimpleVectorStore

# ----------------------------
# Logging (local audit trail)
# ----------------------------
REPO_ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = REPO_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "week5_rag_log.txt"


def log_event(event: str, payload: Dict[str, Any]) -> None:
    """
    Lightweight structured logging for RAG auditing.

    SECURITY NOTE:
    - Logs may contain sensitive or malicious content; keep previews short.
    - Use request_id to correlate all events for a single query.
    """
    ts = datetime.now(timezone.utc).isoformat()
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"Time: {ts}\n")
        f.write(f"Event: {event}\n")
        for k, v in payload.items():
            f.write(f"{k}: {v}\n")


# Requires OPENAI_API_KEY in the environment
client = OpenAI()

EMBED_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"


def get_embedding(text: str, request_id: str) -> List[float]:
    """
    Generate an embedding for a piece of text.

    SECURITY NOTE:
    - Input text may be untrusted (user queries or document content)
    - Embeddings themselves can leak semantic information
    """
    log_event(
        "rag_embedding_request",
        {"request_id": request_id, "input_len": len(text), "input_preview": text[:120]},
    )

    resp = client.embeddings.create(
        model=EMBED_MODEL,
        input=text,
    )
    return resp.data[0].embedding


def build_index() -> SimpleVectorStore:
    """
    Load, chunk, embed, and index all documents.

    SECURITY NOTE:
    - Documents are implicitly trusted at ingestion time
    - This is a critical assumption tested in Week 6 (indirect prompt injection)
    """
    ingestion_id = str(uuid.uuid4())
    log_event("rag_ingestion_start", {"request_id": ingestion_id})

    print("Loading and chunking documents...")
    chunks = load_and_chunk_all()
    store = SimpleVectorStore()

    log_event(
        "rag_ingestion_chunks_loaded",
        {"request_id": ingestion_id, "chunks": len(chunks)},
    )

    print(f"Embedding {len(chunks)} chunks...")
    for i, chunk in enumerate(chunks, start=1):
        # NOTE: Do not log full chunk text; it may be malicious/sensitive.
        emb = get_embedding(chunk["text"], request_id=ingestion_id)
        store.add(
            emb,
            metadata={
                "doc_name": chunk["doc_name"],
                "chunk_index": chunk["chunk_index"],
                # UNTRUSTED CONTENT:
                # Document text may contain malicious instructions
                "text": chunk["text"],
            },
        )

        # Light progress log every N chunks (keeps logs readable)
        if i % 25 == 0 or i == len(chunks):
            log_event(
                "rag_ingestion_progress",
                {"request_id": ingestion_id, "embedded_chunks": i},
            )

    log_event("rag_ingestion_complete", {"request_id": ingestion_id})
    print("Index built.")
    return store


def _format_hits_for_context(top_hits: List[Tuple[float, Dict[str, Any]]]) -> str:
    context_parts: List[str] = []
    for score, item in top_hits:
        meta = item["metadata"]
        # UNTRUSTED CONTEXT (may include malicious instructions)
        context_parts.append(
            f"[{meta['doc_name']} chunk {meta['chunk_index']}] {meta['text']}"
        )
    return "\n\n".join(context_parts)


def rag_query(store: SimpleVectorStore, query: str) -> str:
    """
    Core RAG pipeline.

    TRUST BOUNDARIES:
    - User query is untrusted input
    - Retrieved documents are untrusted context
    - System prompt defines intended safe behavior
    """
    request_id = str(uuid.uuid4())

    log_event(
        "rag_user_input",
        {"request_id": request_id, "user_text": query, "user_len": len(query)},
    )

    # 1) Embed the UNTRUSTED user query
    query_embedding = get_embedding(query, request_id=request_id)

    # 2) Retrieve top-k relevant document chunks
    top_hits = store.top_k(query_embedding, k=3)

    # Log retrieval metadata (NOT full text)
    hit_summaries = []
    for score, item in top_hits:
        meta = item["metadata"]
        hit_summaries.append(
            f"{meta.get('doc_name')}#{meta.get('chunk_index')} score={score:.4f}"
        )

    log_event(
        "rag_retrieval",
        {
            "request_id": request_id,
            "k": 3,
            "hits": len(top_hits),
            "hit_summaries": "; ".join(hit_summaries),
        },
    )

    # 3) Build context from retrieved chunks (UNTRUSTED)
    context = _format_hits_for_context(top_hits)
    log_event(
        "rag_context_built",
        {
            "request_id": request_id,
            "context_len": len(context),
            "context_preview": context[:200],
        },
    )

    # 4) Construct user-facing prompt
    user_prompt = f"""Use the context below to answer the user's question.
If the answer is not in the context, say you are not sure and do not make things up.

Context:
{context}

Question: {query}
Answer:"""

    log_event(
        "rag_prompt_built",
        {
            "request_id": request_id,
            "prompt_len": len(user_prompt),
            "prompt_preview": user_prompt[:200],
        },
    )

    # 5) LLM call
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful cybersecurity and AI security assistant.",
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )

    # 6) Extract model output (treat as untrusted until validated)
    answer_text = response.choices[0].message.content or ""
    answer_text = answer_text.strip()

    # 7) Unified response log (evidence anchor)
    log_event(
        "rag_response",
        {
            "request_id": request_id,
            "output_len": len(answer_text),
            "output_preview": answer_text[:200],
        },
    )

    return answer_text


def main() -> None:
    """
    CLI entry point.

    SECURITY NOTE:
    - Demonstrates full RAG pipeline execution
    - Useful for observing prompt injection behavior interactively
    """
    store = build_index()
    print("\nRAG app over local docs is ready.")

    while True:
        q = input("\nQuestion (or 'q' to quit): ").strip()
        if q.lower() in ("q", "quit", "exit"):
            break
        if not q:
            continue

        answer = rag_query(store, q)
        print("\nAnswer:\n", answer)


if __name__ == "__main__":
    main()
