"""
DARK OS
Memory Search Engine

Encapsula todas las operaciones relacionadas con la búsqueda
de recuerdos.
"""

from __future__ import annotations

from app.memory.models import Memory
from app.memory.repositories.memory_repository import MemoryRepository
from app.memory.search.processor import QueryProcessor
from app.memory.search.scorer import MemoryScorer


class MemorySearchEngine:
    """
    Motor de búsqueda de recuerdos.
    """

    def __init__(self) -> None:

        self.repository = MemoryRepository()
        self.processor = QueryProcessor()
        self.scorer = MemoryScorer()

    def get_recent(
        self,
        limit: int = 5,
    ) -> list[Memory]:
        """
        Devuelve los recuerdos más recientes.
        """

        return self.repository.get_recent(limit)

    def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[Memory]:
        """
        Busca recuerdos relacionados con la consulta.
        """

        # Procesar la consulta del usuario
        processed_query = self.processor.process(query)

        # Buscar candidatos
        memories = self.repository.search(
            processed_query,
            limit * 3,
        )

        # Ordenar por puntuación
        ranked = sorted(
            memories,
            key=lambda memory: self.scorer.score(
                memory,
                processed_query,
            ),
            reverse=True,
        )

        return ranked[:limit]