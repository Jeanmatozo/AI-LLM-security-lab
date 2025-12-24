# src/app_rag_docs/rag_app.py
import datetime
from pathlib import Path
from typing import List

from openai import OpenAI

from .loader import load_and_chunk_all
from .vectorstore import SimpleVectorStore

# Logging directory for auditability and evidence collection
LOG_DIR = Path(__file__).resolve().parents[2] / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "week5_rag_log.txt"

# Requires OPENAI_API_KEY in the environment
client = OpenAI()

EMBED_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"


def get_embedding(text: str) -> List[float]:
    """
    Generate an embedding for a piece of text.

    SECURITY NOTE:
    - Input text may be untrusted (user queries or document content)
    - Embeddings themselves can leak semantic information
    """
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
    print("Loading and chunking documents...")
    chunks = load_and_chunk_all()
    store = SimpleVectorStore()

    print(f"Embedding {len(chunks)} chunks...")
    for chunk in chunks:
        emb = get_embedding(chunk["text"])
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

    print("Index built.")
    return store


def log_result(query: str, context: str, answer: str) -> None:
    """
    Log query, retrieved context, and model response for auditing.

    SECURITY NOTE:
    - Logs are critical for detecting prompt injection and misuse
    - Stored logs may contain sensitive or malicious content
    """
    timestamp = datetime.datetime.now().isoformat()
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"Time: {timestamp}\n")
        f.write(f"Query: {query}\n\n")
        f.write("Context Used:\n")
        f.write(context)
        f.write("\n\nAnswer:\n")
        f.write(answer)
        f.write("\n\n")


def rag_query(store: SimpleVectorStore, query: str) -> str:
    """
    Core RAG pipeline.

    TRUST BOUNDARIES:
    - User query is untrusted input
    - Retrieved documents are untrusted context
    - System prompt defines intended safe behavior
    """
    # 1) Embed the UNTRUSTED user query
    query_embedding = get_embedding(query)

    # 2) Retrieve top-k relevant document chunks
    # TRUST BOUNDARY:
    # Retrieved chunks may contain malicious or instruction-like content
    top_hits = store.top_k(query_embedding, k=3)

    # 3) Build context from retrieved chunks
    context_parts = []
    for score, item in top_hits:
        meta = item["metadata"]
        context_parts.append(
            f"[{meta['doc_name']} chunk {meta['chunk_index']}] {meta['text']}"
        )

    # UNTRUSTED CONTEXT:
    # This text will be concatenated directly into the prompt
    context = "\n\n".join(context_parts)

    # 4) Construct user-facing prompt
    # TRUST BOUNDARY:
    # Untrusted context is combined with trusted instructions
    user_prompt = f"""Use the context below to answer the user's question.
If the answer is not in the context, say you are not sure and do not make things up.

Context:
{context}

Question: {query}
Answer:"""

    # 5) LLM call
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                # TRUSTED SYSTEM MESSAGE
                "role": "system",
                "content": "You are a helpful cybersecurity and AI security assistant.",
            },
            {
                # UNTRUSTED USER MESSAGE (includes retrieved context)
                "role": "user",
                "content": user_prompt,
            },
        ],
    )

    # 6) Extract model output
    # Model output must be treated as untrusted until validated
    answer_text = response.choices[0].message.content

    # 7) Log full execution for review and evidence
    log_result(query, context, answer_text)

    return answer_text


def main():
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

