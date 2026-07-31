"""
DARK OS
Memory AI Schemas
"""

from __future__ import annotations

from dataclasses import dataclass

from app.memory.models import MemoryCategory


@dataclass(slots=True)
class MemoryAIResult:
    """
    Resultado generado por la IA.
    """

    remember: bool

    category: MemoryCategory

    title: str

    content: str

    importance: int