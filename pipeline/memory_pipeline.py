"""
DARK OS
Memory Pipeline

Procesa completamente un mensaje y almacena
recuerdos estructurados.
"""

from __future__ import annotations

from app.memory.models import (
    Conversation,
    ConversationRole,
)

from app.memory.repositories.conversation_repository import (
    ConversationRepository,
)

from app.memory.repositories.memory_repository import (
    MemoryRepository,
)

from app.memory.utils.importance import (
    ImportanceEngine,
)

from app.memory.pipeline.normalizer import (
    MemoryNormalizer,
)

from app.memory.resolver.conflict_resolver import (
    MemoryConflictResolver,
)

from app.memory.resolver.resolution import (
    Resolution,
)

from app.memory.ai.memory_ai import (
    MemoryAI,
)


class MemoryPipeline:
    """
    Pipeline principal encargado del procesamiento
    completo de la memoria.
    """

    def __init__(self) -> None:

        self.conversations = ConversationRepository()
        self.memories = MemoryRepository()

        self.importance = ImportanceEngine()
        self.normalizer = MemoryNormalizer()

        self.memory_ai = MemoryAI()
        self.resolver = MemoryConflictResolver()

    def run(
        self,
        role: ConversationRole,
        content: str,
    ) -> Conversation:
        """
        Procesa completamente un mensaje.
        """

        importance = self.importance.calculate(content)

        conversation = self.conversations.add_message(
            role=role,
            content=content,
            importance=importance,
        )

        if importance < 5:
            return conversation

        memory = self.memory_ai.analyze(content)

        if not memory.remember:
            return conversation

        memory = self.normalizer.normalize(memory)

        decision = self.resolver.resolve(memory)

        if decision == Resolution.IGNORE:
            return conversation

        if decision == Resolution.CREATE:

            self.memories.add_memory(
                category=memory.category,
                title=memory.title,
                content=memory.content,
                importance=memory.importance,
            )

            return conversation

        if decision == Resolution.UPDATE:

            existing = self.memories.find_by_title(
                memory.title,
            )

            if existing is not None:

                existing.category = memory.category
                existing.content = memory.content
                existing.importance = memory.importance

                self.memories.update_memory(existing)

        return conversation