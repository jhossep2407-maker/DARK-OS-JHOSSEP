"""
DARK OS
Kernel
"""

from __future__ import annotations

from enum import Enum, auto

from app.core.lifecycle import LifecycleManager
from app.core.logger import logger


class KernelState(Enum):
    OFF = auto()
    BOOTING = auto()
    READY = auto()
    SHUTDOWN = auto()


class Kernel:
    """
    Núcleo principal de DARK OS.
    """

    def __init__(self) -> None:
        self.state = KernelState.OFF
        self.lifecycle = LifecycleManager()

    def boot(self) -> None:
        logger.info("Kernel Boot")

        self.state = KernelState.BOOTING

        self.lifecycle.startup()

        self.state = KernelState.READY

        logger.info("Kernel Ready")

    def shutdown(self) -> None:
        logger.info("Kernel Shutdown")

        self.lifecycle.shutdown()

        self.state = KernelState.SHUTDOWN


kernel = Kernel()