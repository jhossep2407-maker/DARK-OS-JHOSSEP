"""
DARK OS
Memory Service
"""

from __future__ import annotations

from app.memory.models import Conversation, ConversationRole
from app.memory.pipeline.memory_pipeline import MemoryPipeline


class MemoryService:

    def __init__(self):

        self.pipeline = MemoryPipeline()

    def process_message(
        self,
        role: ConversationRole,
        content: str,
    ) -> Conversation:

        return self.pipeline.run(
            role=role,
            content=content,
        )