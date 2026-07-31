"""
DARK OS
Memory Conflict Resolver
"""

from __future__ import annotations

from app.memory.models import Memory
from app.memory.repositories.memory_repository import MemoryRepository
from app.memory.resolver.resolution import Resolution


class MemoryConflictResolver:
    """
    Decide qué hacer con un nuevo recuerdo.

    Puede indicar:

    - CREATE
    - UPDATE
    - IGNORE
    """

    def __init__(self) -> None:

        self.repository = MemoryRepository()

    def resolve(
        self,
        memory: Memory,
    ) -> Resolution:
        """
        Analiza un recuerdo nuevo y decide
        qué acción debe realizarse.
        """

        existing = self.repository.find_by_title(
            memory.title,
        )

        if existing is None:
            return Resolution.CREATE

        if existing.content.lower() == memory.content.lower():
            return Resolution.IGNORE

        return Resolution.UPDATE