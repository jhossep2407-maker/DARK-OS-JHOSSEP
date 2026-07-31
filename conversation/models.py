"""
DARK OS
Conversation Models
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConversationMessage:

    role: str

    content: str