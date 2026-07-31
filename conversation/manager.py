"""
DARK OS
Conversation Manager
"""

from __future__ import annotations

from app.ai.orchestrator import AIOrchestrator

from app.memory.models import ConversationRole
from app.memory.pipeline.memory_pipeline import MemoryPipeline

from app.conversation.conversation_brain import ConversationBrain


class ConversationManager:

    def __init__(self) -> None:

        self.ai = AIOrchestrator()

        self.memory = MemoryPipeline()

        self.brain = ConversationBrain()

    def chat(
        self,
        message: str,
    ) -> str:

        # Guardar mensaje del usuario
        self.memory.run(
            ConversationRole.USER,
            message,
        )

        # Agregar al historial corto
        self.brain.add_user(
            message,
        )

        # Obtener conversación completa
        conversation = self.brain.context()

        # Enviar a la IA
        response = self.ai.chat(
            user_message=message,
            conversation=conversation,
        )

        if response is None:

            response = (
                "Lo siento, ocurrió un error."
            )

        # Agregar respuesta al historial
        self.brain.add_assistant(
            response,
        )

        # Guardar memoria
        self.memory.run(
            ConversationRole.ASSISTANT,
            response,
        )

        return response