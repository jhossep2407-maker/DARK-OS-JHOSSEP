"""
DARK OS
Memory Search Scorer
"""

from __future__ import annotations

from datetime import datetime

from app.memory.models import Memory


class MemoryScorer:
    """
    Calcula la puntuación de un recuerdo.
    """

    RELEVANCE_WEIGHT = 0.60
    IMPORTANCE_WEIGHT = 0.30
    RECENCY_WEIGHT = 0.10

    def score(
        self,
        memory: Memory,
        query: str,
    ) -> float:

        relevance = self._relevance(memory, query)

        importance = self._importance(memory)

        recency = self._recency(memory)

        return (
            relevance * self.RELEVANCE_WEIGHT
            + importance * self.IMPORTANCE_WEIGHT
            + recency * self.RECENCY_WEIGHT
        )

    def _relevance(
        self,
        memory: Memory,
        query: str,
    ) -> float:

        score = 0

        query = query.lower()

        if query in memory.title.lower():
            score += 50

        if query in memory.content.lower():
            score += 100

        return score

    def _importance(
        self,
        memory: Memory,
    ) -> float:

        return memory.importance * 20

    def _recency(
        self,
        memory: Memory,
    ) -> float:
        """
        Calcula una puntuación simple según la antigüedad.
        """

        if not hasattr(memory, "created_at"):
            return 50

        days = (datetime.utcnow() - memory.created_at).days

        return max(0, 100 - days)