"""
DARK OS
Memory Gate
"""

from __future__ import annotations


class MemoryGate:
    """
    Decide si una consulta necesita acceder
    a la memoria de largo plazo.
    """

    def __init__(self) -> None:

        self.keywords = (

            # Memoria
            "recuerdas",
            "recordar",
            "recuerdo",
            "memoria",

            # Usuario
            "mi ",
            "mis ",

            # Preferencias
            "favorito",
            "favorita",
            "gusta",
            "prefiero",

            # Proyectos
            "proyecto",
            "trabajando",
            "desarrollando",
            "creando",

            # Objetivos
            "meta",
            "objetivo",
            "aprendiendo",

            # Preguntas típicas
            "qué sabes",
            "que sabes",
            "quién soy",
            "quien soy",
        )

    def should_search(
        self,
        message: str,
    ) -> bool:
        """
        Devuelve True si la memoria debe
        consultarse.
        """

        message = message.lower()

        return any(
            keyword in message
            for keyword in self.keywords
        )