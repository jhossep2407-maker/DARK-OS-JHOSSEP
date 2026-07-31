"""
DARK OS
Memory Resolution
"""

from __future__ import annotations

from enum import Enum


class Resolution(str, Enum):
    """
    Posibles acciones que puede tomar el
    resolvedor de memoria.
    """

    CREATE = "create"
    UPDATE = "update"
    IGNORE = "ignore"