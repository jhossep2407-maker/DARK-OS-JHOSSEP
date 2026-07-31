"""
DARK OS
Memory Data
"""

from __future__ import annotations

from dataclasses import dataclass

from app.memory.models import MemoryCategory


@dataclass(slots=True)
class MemoryData:
    """
    Representa un recuerdo extraído de un mensaje.
    """

    category: MemoryCategory
    title: str
    content: str