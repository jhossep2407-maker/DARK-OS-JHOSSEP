"""
DARK OS
Conversation Repository

Gestiona todas las operaciones relacionadas con la tabla
Conversation.
"""

from __future__ import annotations

from app.memory.database import get_session
from app.memory.models import Conversation, ConversationRole


class ConversationRepository:
    """
    Repositorio para gestionar conversaciones.
    """

    def add_message(
        self,
        role: ConversationRole,
        content: str,
        importance: int = 5,
    ) -> Conversation:
        """
        Guarda un nuevo mensaje en la base de datos.
        """

        message = Conversation(
            role=role,
            content=content,
            importance=importance,
        )

        with get_session() as session:
            session.add(message)
            session.flush()
            session.refresh(message)

        return message

    def get_by_id(
        self,
        message_id: int,
    ) -> Conversation | None:
        """
        Obtiene un mensaje por su ID.
        """

        with get_session() as session:
            return session.get(Conversation, message_id)
    def get_recent_messages(
        self,
        limit: int = 10,
    ) -> list[Conversation]:
        """
        Devuelve los últimos mensajes ordenados
        del más reciente al más antiguo.
        """

        with get_session() as session:
            return (
                session.query(Conversation)
                .order_by(Conversation.created_at.desc())
                .limit(limit)
                .all()
            )
    def count(self) -> int:
        """
        Devuelve el número total de conversaciones.
        """

        with get_session() as session:
            return session.query(Conversation).count()
    def delete_by_id(self, message_id: int) -> bool:
        """
        Elimina un mensaje por su ID.

        Returns:
            True si el mensaje existía y fue eliminado,
            False si no existía.
        """

        with get_session() as session:
            message = session.get(Conversation, message_id)

            if message is None:
                return False

            session.delete(message)
            return True
    def delete_all(self) -> int:
        """
        Elimina todas las conversaciones.

        Returns:
            Cantidad de mensajes eliminados.
        """

        with get_session() as session:
            deleted = session.query(Conversation).delete()
            return deleted