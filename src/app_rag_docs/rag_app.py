# src/app_rag_docs/rag_app.py
import datetime
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parents[2] / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "week5_rag_log.txt"


from typing import List

from openai import OpenAI  # make sure this matches your existing code

from .loader import load_and_chunk_all
from .vectorstore import SimpleVectorStore

# Requires OPENAI_API_KEY in your environment for the client to work
client = OpenAI()

EMBED_MODEL = "text-embedding-3-small"  # adjust if you use a different embedding model
CHAT_MODEL = "gpt-4o-mini"              # adjust to whatever you use in chatbot.py


def get_embedding(text: str) -> List[float]:
    """
    Get an embedding vector for a given piece of text.
    """
    resp = client.embeddings.create(
        model=EMBED_MODEL,
        input=text,
    )
    return resp.data[0].embedding


def build_index() -> SimpleVectorStore:
    """
    Load and chunk all local docs, embed them, and store them in a SimpleVectorStore.
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
                "text": chunk["text"],
            },
        )

    print("Index built.")
    return store
    
def log_result(query: str, context: str, answer: str) -> None:
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
    Core RAG logic:
    - embed the user's query
    - retrieve relevant chunks from the vector store
    - build a context-aware prompt
    - ask the LLM and return the answer
    """
    # 1) Embed the query
    query_embedding = get_embedding(query)

    # 2) Retrieve top-k relevant chunks
    top_hits = store.top_k(query_embedding, k=3)

    # 3) Build context string from the retrieved chunks
    context_parts = []
    for score, item in top_hits:
        meta = item["metadata"]
        context_parts.append(
            f"[{meta['doc_name']} chunk {meta['chunk_index']}] {meta['text']}"
        )

    context = "\n\n".join(context_parts)

    # 4) Construct the final prompt for the LLM
    user_prompt = f"""Use the context below to answer the user's question.
If the answer is not in the context, say you are not sure and do not make things up.

Context:
{context}

Question: {query}
Answer:"""

        # 5) Call the LLM API
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful cybersecurity and AI security assistant.",
            },
            {"role": "user", "content": user_prompt},
        ],
    )

    # 6) Extract answer text
    answer_text = response.choices[0].message.content

    # 7) Log the result (query, context, answer)
    log_result(query, context, answer_text)

    # 8) Return the LLM's answer text
    return answer_text



def main():
    """
    Build the index once, then enter a CLI loop to answer questions via rag_query.
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
