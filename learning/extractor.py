"""
DARK OS
Learning Extractor
"""

from __future__ import annotations

from app.memory.models import MemoryCategory


class LearningExtractor:
    """
    Extrae posibles recuerdos de un texto.
    """

    def extract(
        self,
        text: str,
    ) -> list[dict]:
        """
        Extrae recuerdos simples.
        """

        return [
            {
                "category": MemoryCategory.PREFERENCE,
                "title": "Información aprendida",
                "content": text,
            }
        ]