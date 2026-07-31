"""
DARK OS
Chat Service
"""

from __future__ import annotations

from app.ai.orchestrator import AIOrchestrator


class ChatService:
    """
    Servicio público de conversación.
    """

    def __init__(self) -> None:

        self.orchestrator = AIOrchestrator()

    def chat(
        self,
        message: str,
    ) -> str:

        return self.orchestrator.process(message)