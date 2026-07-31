"""
DARK OS
Service Container
"""

from __future__ import annotations

from typing import Any

from app.memory.services.memory_service import MemoryService


class ServiceContainer:
    """
    Contenedor principal de servicios.
    """

    def __init__(self) -> None:

        self._services: dict[str, Any] = {}

        # Registrar servicios base
        self.register("memory", MemoryService())

    def register(
        self,
        name: str,
        service: Any,
    ) -> None:
        """
        Registra un servicio.
        """

        self._services[name] = service

    def get(self, name: str) -> Any:
        """
        Devuelve un servicio.
        """

        return self._services[name]

    def __getattr__(self, name: str) -> Any:
        """
        Permite acceder como:

        container.memory
        """

        if name in self._services:
            return self._services[name]

        raise AttributeError(f"Servicio '{name}' no registrado.")


container = ServiceContainer()
