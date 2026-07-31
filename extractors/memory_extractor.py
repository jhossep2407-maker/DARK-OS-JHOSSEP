"""
DARK OS
Memory Extractor

Extrae recuerdos estructurados desde mensajes del usuario.
"""

from __future__ import annotations

import re

from app.memory.models import MemoryCategory
from app.memory.extractors.memory_data import MemoryData


class MemoryExtractor:
    """
    Extrae recuerdos estructurados.
    """

    def extract(
        self,
        text: str,
    ) -> MemoryData:

        original = text.strip()
        lower = original.lower()

        # ==========================================
        # COLOR FAVORITO
        # ==========================================

        match = re.search(
            r"mi color favorito es (.+)",
            lower,
        )

        if match:

            return MemoryData(
                category=MemoryCategory.PREFERENCE,
                title="Color favorito",
                content=match.group(1).strip().capitalize(),
            )

        # ==========================================
        # COMIDA FAVORITA
        # ==========================================

        match = re.search(
            r"mi comida favorita es (.+)",
            lower,
        )

        if match:

            return MemoryData(
                category=MemoryCategory.PREFERENCE,
                title="Comida favorita",
                content=match.group(1).strip().capitalize(),
            )

        # ==========================================
        # LENGUAJE FAVORITO
        # ==========================================

        match = re.search(
            r"mi lenguaje favorito es (.+)",
            lower,
        )

        if match:

            return MemoryData(
                category=MemoryCategory.PREFERENCE,
                title="Lenguaje favorito",
                content=match.group(1).strip(),
            )

        # ==========================================
        # PROYECTOS
        # ==========================================

        match = re.search(
            r"estoy creando (.+)",
            lower,
        )

        if match:

            return MemoryData(
                category=MemoryCategory.PROJECT,
                title="Proyecto",
                content=match.group(1).strip().upper(),
            )

        # ==========================================
        # APRENDIZAJE
        # ==========================================

        match = re.search(
            r"estoy aprendiendo (.+)",
            lower,
        )

        if match:

            return MemoryData(
                category=MemoryCategory.GOAL,
                title="Aprendiendo",
                content=match.group(1).strip(),
            )

        # ==========================================
        # POR DEFECTO
        # ==========================================

        return MemoryData(
            category=MemoryCategory.FACT,
            title="Información",
            content=original,
        )