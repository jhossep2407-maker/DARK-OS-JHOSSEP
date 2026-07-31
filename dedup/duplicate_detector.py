"""
DARK OS
Duplicate Detector
"""

from __future__ import annotations

from app.memory.repositories.memory_repository import MemoryRepository


class DuplicateDetector:
    """
    Detecta si un recuerdo ya existe.
    """

    def __init__(self) -> None:

        self.repository = MemoryRepository()

    def exists(
        self,
        title: str,
        content: str,
    ) -> bool:
        """
        Devuelve True si ya existe un recuerdo
        con el mismo título y contenido.
        """

        memory = self.repository.find_by_title(title)

        if memory is None:
            return False

        return memory.content.lower() == content.lower()