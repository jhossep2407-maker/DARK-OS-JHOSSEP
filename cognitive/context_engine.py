"""
DARK OS
Context Engine
"""

from __future__ import annotations

from app.context.memory_gate import MemoryGate
from app.memory.search.search_engine import MemorySearchEngine


class ContextEngine:

    def __init__(self):

        self.gate = MemoryGate()
        self.memory = MemorySearchEngine()

    def build(
        self,
        message: str,
    ) -> str:

        if not self.gate.should_search(message):
            return ""

        memories = self.memory.search(message)

        if not memories:
            return ""

        block = ""

        for memory in memories:

            block += (
                f"- {memory.title}: "
                f"{memory.content}\n"
            )

        return block