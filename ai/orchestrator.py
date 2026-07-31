"""
DARK OS
AI Orchestrator
"""

from __future__ import annotations

from app.ai.router import AIRouter
from app.cognitive.core import CognitiveCore


class AIOrchestrator:
    """
    Orquestador principal de IA.
    """

    def __init__(self) -> None:

        self.router = AIRouter()

        self.cognitive = CognitiveCore()

    def chat(
        self,
        user_message: str,
        conversation: str = "",
    ) -> str:

        prompt = self.cognitive.process(
            message=user_message,
            conversation=conversation,
        )

        return self.router.provider.chat(
            prompt,
        )