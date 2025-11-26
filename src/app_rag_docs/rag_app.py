# src/app_rag_docs/rag_app.py

from typing import List

from openai import OpenAI  # make sure this matches your existing code

from .loader import load_and_chunk_all
from .vectorstore import SimpleVectorStore

client = OpenAI()  # requires OPENAI_API_KEY in your environment

EMBED_MODEL = "text-embedding-3-small"  # adjust if you use a different embedding model
CHAT_MODEL = "gpt-4o-mini"              # adjust to whatever you use in chatbot.py


def get_embedding(text: str) -> List[float]:
    resp = client.embeddings.create(
        model=EMBED_MODEL,
        input=text,
    )
    return resp.data[0].embedding


def build_index() -> SimpleVectorStore:
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


def answer_question(store: SimpleVectorStore, question: str) -> str:
    q_emb = get_embedding(question)
    top = store.top_k(q_emb, k=3)

    context_parts = []
    for score, item in top:
        meta = item["metadata"]
        context_parts.append(
            f"[{meta['doc_name']} chunk {meta['chunk_index']}] {meta['text']}"
        )

    context = "\n\n".join(context_parts)

    user_prompt = f"""Use the context below to answer the user's question.
If the answer is not in the context, say you are not sure and do not make things up.

Context:
{context}

Question: {question}
Answer:"""

    resp = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful cybersecurity and AI security assistant.",
            },
            {"role": "user", "content": user_prompt},
        ],
    )
    return resp.choices[0].message.content


def main():
    store = build_index()
    print("\nRAG app over local docs is ready.")

    while True:
        q = input("\nQuestion (or 'q' to quit): ").strip()
        if q.lower() in ("q", "quit", "exit"):
            break
        if not q:
            continue

        answer = answer_question(store, q)
        print("\nAnswer:\n", answer)


if __name__ == "__main__":
    main()

