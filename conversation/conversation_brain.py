"""
DARK OS
Conversation Brain
"""

from __future__ import annotations

from collections import deque


class ConversationBrain:

    def __init__(
        self,
        max_messages: int = 12,
    ) -> None:

        self.history = deque(
            maxlen=max_messages,
        )

    def add_user(
        self,
        message: str,
    ) -> None:

        self.history.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant(
        self,
        message: str,
    ) -> None:

        self.history.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def context(self) -> str:

        if not self.history:
            return ""

        text = []

        for item in self.history:

            if item["role"] == "user":

                text.append(
                    f"Usuario: {item['content']}"
                )

            else:

                text.append(
                    f"DARK: {item['content']}"
                )

        return "\n".join(text)

    def clear(self) -> None:

        self.history.clear()