"""
DARK OS
Memory Models

Define las entidades persistentes del sistema utilizando
SQLAlchemy ORM 2.0.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum as SQLEnum,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# ==========================================================
# Base ORM
# ==========================================================

class Base(DeclarativeBase):
    """
    Clase base para todos los modelos ORM de DARK OS.
    """
    pass


# ==========================================================
# Enumeraciones
# ==========================================================

class ConversationRole(str, Enum):
    """
    Roles permitidos en una conversación.
    """

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class MemoryType(str, Enum):
    """
    Tipos de memoria soportados por DARK.
    """

    SHORT_TERM = "short_term"
    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    PROFILE = "profile"
    SYSTEM = "system"


# ==========================================================
# Conversation
# ==========================================================

class Conversation(Base):
    """
    Representa un mensaje dentro de una conversación.
    """

    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    role: Mapped[ConversationRole] = mapped_column(
        SQLEnum(ConversationRole),
        nullable=False,
        index=True,
    )
    
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
    )

    importance: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False,
    )

    encrypted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    summarized: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    embedding_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    metadata_json: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    def __repr__(self) -> str:
        return (
            f"<Conversation(id={self.id}, "
            f"role='{self.role.value}', "
            f"importance={self.importance})>"
        )
    

class MemoryCategory(str, Enum):
    """
    Categorías de recuerdos almacenados.
    """

    FACT = "fact"
    PROJECT = "project"
    GOAL = "goal"
    PREFERENCE = "preference"
    EVENT = "event"
    SYSTEM = "system"

class Memory(Base):
    """
    Representa un recuerdo importante extraído de las conversaciones.
    """

    __tablename__ = "memories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    category: Mapped[MemoryCategory] = mapped_column(
        SQLEnum(MemoryCategory),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    importance: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    last_accessed: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    access_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    embedding_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    metadata_json: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    def __repr__(self) -> str:
        return (
            f"<Memory(id={self.id}, "
            f"category='{self.category.value}', "
            f"importance={self.importance})>"
        )