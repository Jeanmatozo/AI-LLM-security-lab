# src/app_rag_docs/vectorstore.py

import math
from typing import List, Dict, Tuple, Any


def cosine_similarity(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


class SimpleVectorStore:
    def __init__(self):
        # each item: {"embedding": List[float], "metadata": Dict[str, Any]}
        self.items: List[Dict[str, Any]] = []

    def add(self, embedding: List[float], metadata: Dict[str, Any]) -> None:
        self.items.append(
            {
                "embedding": embedding,
                "metadata": metadata,
            }
        )

    def top_k(
        self, query_embedding: List[float], k: int = 3
    ) -> List[Tuple[float, Dict[str, Any]]]:
        scored: List[Tuple[float, Dict[str, Any]]] = []

        for item in self.items:
            score = cosine_similarity(query_embedding, item["embedding"])
            scored.append((score, item))

        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[:k]

