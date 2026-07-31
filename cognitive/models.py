"""
DARK OS
Cognitive Models
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CognitiveState:
    """
    Estado cognitivo actual.
    """

    user_message: str

    intent: str = "conversation"

    use_memory: bool = False

    use_tools: bool = False

    use_planner: bool = False

    context: str = ""

    response: str = ""