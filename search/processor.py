"""
DARK OS
Query Processor

Preprocesa las consultas del usuario antes de buscar
recuerdos en la memoria.
"""

from __future__ import annotations

import re


class QueryProcessor:
    """
    Limpia y simplifica las consultas del usuario.
    """

    STOPWORDS = {
        "que",
        "qué",
        "cual",
        "cuál",
        "es",
        "mi",
        "mis",
        "el",
        "la",
        "los",
        "las",
        "un",
        "una",
        "unos",
        "unas",
        "de",
        "del",
        "al",
        "en",
        "y",
        "o",
        "a",
        "sobre",
        "acerca",
        "como",
        "cómo",
        "me",
        "te",
        "tu",
        "tú",
    }

    def process(
        self,
        query: str,
    ) -> str:
        """
        Convierte una pregunta en palabras clave.
        """

        # Minúsculas
        query = query.lower()

        # Eliminar signos de puntuación
        query = re.sub(r"[^\w\s]", "", query)

        # Separar palabras
        words = query.split()

        # Eliminar palabras vacías
        keywords = [
            word
            for word in words
            if word not in self.STOPWORDS
        ]

        return " ".join(keywords)