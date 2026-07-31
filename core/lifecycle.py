"""
DARK OS
Lifecycle Manager
"""

from __future__ import annotations

from app.core.logger import logger


class LifecycleManager:
    """
    Controla el ciclo de vida del sistema.
    """

    def startup(self) -> None:
        logger.info("Starting DARK OS...")

    def shutdown(self) -> None:
        logger.info("Stopping DARK OS...")