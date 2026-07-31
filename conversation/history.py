"""
DARK OS
Conversation History
"""

from __future__ import annotations

from collections import deque

from app.conversation.models import (
    ConversationMessage,
)


class ConversationHistory:

    def __init__(
        self,
        limit: int = 20,
    ) -> None:

        self.messages = deque(
            maxlen=limit,
        )

    def add_user(
        self,
        text: str,
    ) -> None:

        self.messages.append(
            ConversationMessage(
                role="Usuario",
                content=text,
            )
        )

    def add_assistant(
        self,
        text: str,
    ) -> None:

        self.messages.append(
            ConversationMessage(
                role="DARK",
                content=text,
            )
        )

    def clear(self) -> None:

        self.messages.clear()

    def build(self) -> str:

        if not self.messages:
            return ""

        result = ""

        for message in self.messages:

            result += (
                f"{message.role}: "
                f"{message.content}\n"
            )

        return result.strip()