"""
DARK OS
AI Router
"""

from __future__ import annotations

from app.core.config import settings

from app.ai.providers.base import BaseAIProvider
from app.ai.providers.gemini_provider import GeminiProvider
from app.ai.providers.glm_provider import GLMProvider


class AIRouter:
    """
    Selecciona automáticamente el proveedor
    principal de inteligencia artificial.
    """

    def __init__(self) -> None:

        provider = settings.ai.provider.lower()

        providers: dict[str, type[BaseAIProvider]] = {
            "gemini": GeminiProvider,
            "glm": GLMProvider,
        }

        provider_class = providers.get(provider)

        if provider_class is None:

            raise ValueError(
                f"Proveedor '{provider}' no soportado."
            )

        self.provider = provider_class()