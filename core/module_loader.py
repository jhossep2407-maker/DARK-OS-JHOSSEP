"""
DARK OS
Module Loader

Se encarga de registrar e inicializar todos los módulos del sistema.
"""

from __future__ import annotations

from typing import Protocol

from app.core.logger import logger


class Module(Protocol):
    """
    Interfaz que debe implementar cualquier módulo.
    """

    def initialize(self) -> None:
        ...


class ModuleLoader:
    """
    Administra los módulos del sistema.
    """

    def __init__(self) -> None:
        self._modules: dict[str, Module] = {}

    def register(self, name: str, module: Module) -> None:
        """
        Registra un módulo.
        """
        self._modules[name] = module
        logger.info(f"Module registered -> {name}")

    def initialize_all(self) -> None:
        """
        Inicializa todos los módulos registrados.
        """
        logger.info("Initializing modules...")

        for name, module in self._modules.items():
            logger.info(f"Initializing -> {name}")
            module.initialize()

        logger.info("All modules initialized.")


module_loader = ModuleLoader()