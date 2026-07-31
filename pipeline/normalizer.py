"""
DARK OS
Memory Normalizer

Normaliza los recuerdos antes de almacenarlos.
"""

from __future__ import annotations

import re

from app.memory.ai.schemas import MemoryAIResult


class MemoryNormalizer:
    """
    Normaliza un recuerdo generado por la IA.
    """

    def normalize(
        self,
        memory: MemoryAIResult,
    ) -> MemoryAIResult:
        """
        Limpia y estandariza un recuerdo.
        """

        memory.title = self._normalize_title(
            memory.title,
        )

        memory.content = self._normalize_content(
            memory.content,
        )

        return memory

    def _normalize_title(
        self,
        text: str,
    ) -> str:

        text = text.strip()

        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        text = text.rstrip(".")

        if text:

            text = text[0].upper() + text[1:]

        return text

    def _normalize_content(
        self,
        text: str,
    ) -> str:

        text = text.strip()

        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        text = text.rstrip(".")

        for article in (
            "el ",
            "la ",
            "los ",
            "las ",
            "un ",
            "una ",
        ):

            if text.lower().startswith(article):

                text = text[len(article):]

                break

        # Casos especiales

        if text.lower() == "dark os":
            return "DARK OS"

        if text.lower() == "sqlalchemy":
            return "SQLAlchemy"

        if text.lower() == "python":
            return "Python"

        if text:

            text = text[0].upper() + text[1:]

        return text