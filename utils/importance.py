"""
DARK OS
Importance Engine

Calcula la importancia de un mensaje.
"""

from __future__ import annotations


class ImportanceEngine:
    """
    Motor encargado de estimar la importancia
    de un mensaje.
    """

    KEYWORDS = (
        "mi",
        "proyecto",
        "objetivo",
        "recuerda",
        "importante",
        "favorito",
        "nombre",
        "trabajo",
        "estudio",
        "familia",
    )

    def calculate(self, text: str) -> int:
        """
        Devuelve una importancia entre 1 y 10.
        """

        score = 1

        text = text.lower()

        for keyword in self.KEYWORDS:
            if keyword in text:
                score += 2

        score += min(len(text) // 80, 3)

        return min(score, 10)