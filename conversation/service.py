"""
DARK OS
Conversation Service
"""

from __future__ import annotations

from app.conversation.manager import ConversationManager


class ConversationService:

    def __init__(self) -> None:

        self.manager = ConversationManager()

    def chat(
        self,
        message: str,
    ) -> str:

        return self.manager.chat(
            message,
        )