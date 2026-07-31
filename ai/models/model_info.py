"""
DARK OS
Model Information
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ModelInfo:
    """
    Representa un modelo de IA disponible.
    """

    provider: str

    name: str

    priority: int = 0

    enabled: bool = True

    rpm: int = 0

    rpd: int = 0

    context_window: int = 0

    supports_tools: bool = False

    supports_vision: bool = False

    supports_thinking: bool = False

    supports_streaming: bool = True

    def __str__(self) -> str:

        return f"{self.provider}:{self.name}"