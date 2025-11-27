# src/app_rag_docs/vectorstore.py
import math
from typing import List, Dict

def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

class SimpleVectorStore:
    def __init__(self):
        self.items: List[Dict] = []

    def add(self, embedding, metadata):
        self.items.append({
            "embedding": embedding,
            "metadata": metadata,
        })

    def top_k(self, query_embedding, k: int = 3):
        scored = []
        for item in self.items:
            score = cosine_similarity(query_embedding, item["embedding"])
            scored.append((score, item))
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[:k]


