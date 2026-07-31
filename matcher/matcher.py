"""
DARK OS
Memory Matcher
"""

from __future__ import annotations

from difflib import SequenceMatcher

from app.memory.models import Memory
from app.memory.repositories.memory_repository import MemoryRepository


class MemoryMatcher:
    """
    Busca el recuerdo más parecido al nuevo.
    """

    def __init__(self) -> None:

        self.repository = MemoryRepository()

    def similarity(
        self,
        a: str,
        b: str,
    ) -> float:
        """
        Calcula la similitud entre dos textos.
        """

        return SequenceMatcher(
            None,
            a.lower(),
            b.lower(),
        ).ratio()

    def find_best_match(
        self,
        memory: Memory,
    ) -> tuple[Memory | None, float]:
        """
        Devuelve el recuerdo más parecido
        junto con su puntuación.
        """

        memories = self.repository.get_recent(
            limit=1000,
        )

        best_memory = None
        best_score = 0.0

        for existing in memories:

            title_score = self.similarity(
                memory.title,
                existing.title,
            )

            content_score = self.similarity(
                memory.content,
                existing.content,
            )

            score = (
                title_score * 0.6
                + content_score * 0.4
            )

            if score > best_score:

                best_score = score
                best_memory = existing

        if best_score < 0.75:
            return None, best_score

        return best_memory, best_score