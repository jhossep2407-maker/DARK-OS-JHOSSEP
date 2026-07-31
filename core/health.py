"""
DARK OS
Health Check

Verifica el estado de los módulos del sistema.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.core.logger import logger


@dataclass(slots=True)
class HealthStatus:
    name: str
    healthy: bool


class HealthCheck:

    def __init__(self) -> None:
        self._checks: list[HealthStatus] = []

    def register(self, name: str, healthy: bool = True) -> None:
        self._checks.append(HealthStatus(name, healthy))

    def run(self) -> bool:
        logger.info("Running Health Check...")

        all_ok = True

        for check in self._checks:

            if check.healthy:
                logger.info(f"[OK] {check.name}")
            else:
                logger.error(f"[FAIL] {check.name}")
                all_ok = False

        return all_ok


health = HealthCheck()