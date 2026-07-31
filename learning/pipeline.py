"""
DARK OS
Learning Pipeline
"""

from __future__ import annotations

from app.learning.extractor import LearningExtractor
from app.memory.repositories.memory_repository import MemoryRepository


class LearningPipeline:

    def __init__(self):

        self.extractor = LearningExtractor()
        self.repository = MemoryRepository()

    def process(
        self,
        text: str,
    ) -> None:

        memories = self.extractor.extract(text)

        for memory in memories:

            self.repository.add_memory(
                category=memory["category"],
                title=memory["title"],
                content=memory["content"],
                importance=5,
            )