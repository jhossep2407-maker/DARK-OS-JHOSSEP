"""
DARK OS
Memory AI Parser
"""

from __future__ import annotations

import json
import re

from app.memory.ai.schemas import MemoryAIResult
from app.memory.models import MemoryCategory


class MemoryAIParser:
    """
    Convierte la respuesta de la IA en
    un objeto MemoryAIResult.
    """

    def parse(
        self,
        text: str,
    ) -> MemoryAIResult:

        text = text.strip()

        # ----------------------------------
        # Eliminar bloques Markdown
        # ----------------------------------

        text = re.sub(
            r"^```json\s*",
            "",
            text,
            flags=re.IGNORECASE,
        )

        text = re.sub(
            r"^```",
            "",
            text,
        )

        text = re.sub(
            r"```$",
            "",
            text,
        )

        text = text.strip()

        # ----------------------------------
        # Buscar el primer objeto JSON
        # ----------------------------------

        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No se encontró un objeto JSON válido.")

        text = text[start:end + 1]

        data = json.loads(text)

        return MemoryAIResult(
            remember=data["remember"],
            category=MemoryCategory(data["category"].lower()),
            title=data["title"],
            content=data["content"],
            importance=int(data["importance"]),
        )