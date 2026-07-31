"""
DARK OS
Conversation Brain
"""

from __future__ import annotations

from app.conversation.history import (
    ConversationHistory,
)


class ConversationBrain:

    def __init__(self) -> None:

        self.history = ConversationHistory()

    def add_user(
        self,
        text: str,
    ) -> None:

        self.history.add_user(text)

    def add_assistant(
        self,
        text: str,
    ) -> None:

        self.history.add_assistant(text)

    def context(self) -> str:

        return self.history.build()

    def reset(self) -> None:

        self.history.clear()