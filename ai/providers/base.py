"""
DARK OS
Base AI Provider
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseAIProvider(ABC):
    """
    Clase base para todos los proveedores de IA.
    """

    @abstractmethod
    def chat(
        self,
        message: str,
    ) -> str:
        """
        Envía un mensaje al modelo
        y devuelve la respuesta.
        """
        raise NotImplementedError