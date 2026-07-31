"""
DARK OS
Memory Repository

Gestiona todas las operaciones relacionadas con la tabla Memory.
"""

from __future__ import annotations

from sqlalchemy import or_, select

from app.memory.database import get_session
from app.memory.models import Memory, MemoryCategory


class MemoryRepository:
    """
    Repositorio para gestionar los recuerdos almacenados.
    """

    def add_memory(
        self,
        category: MemoryCategory,
        title: str,
        content: str,
        importance: int = 5,
    ) -> Memory:
        """
        Guarda un nuevo recuerdo.
        """

        memory = Memory(
            category=category,
            title=title,
            content=content,
            importance=importance,
        )

        with get_session() as session:
            session.add(memory)
            session.flush()
            session.refresh(memory)

            return memory

    def get_by_id(
        self,
        memory_id: int,
    ) -> Memory | None:
        """
        Obtiene un recuerdo por su ID.
        """

        with get_session() as session:
            return session.get(Memory, memory_id)

    def get_recent(
        self,
        limit: int = 5,
    ) -> list[Memory]:
        """
        Devuelve los recuerdos más recientes.
        """

        with get_session() as session:

            stmt = (
                select(Memory)
                .order_by(Memory.id.desc())
                .limit(limit)
            )

            return list(session.execute(stmt).scalars().all())

    def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[Memory]:
        """
        Busca recuerdos relacionados con una consulta.
        """

        with get_session() as session:

            stmt = (
                select(Memory)
                .where(
                    or_(
                        Memory.title.ilike(f"%{query}%"),
                        Memory.content.ilike(f"%{query}%"),
                    )
                )
                .order_by(Memory.importance.desc())
                .limit(limit)
            )

            return list(session.execute(stmt).scalars().all())

    def find_by_title(
        self,
        title: str,
    ) -> Memory | None:
        """
        Busca un recuerdo por su título.
        """

        with get_session() as session:

            stmt = (
                select(Memory)
                .where(Memory.title == title)
            )

            return session.execute(stmt).scalars().first()

    def update_memory(
        self,
        memory: Memory,
    ) -> Memory:
        """
        Guarda los cambios realizados sobre un recuerdo.
        """

        with get_session() as session:

            updated = session.merge(memory)
            session.flush()
            session.refresh(updated)

            return updated

    def delete(
        self,
        memory_id: int,
    ) -> bool:
        """
        Elimina un recuerdo por su ID.
        """

        with get_session() as session:

            memory = session.get(Memory, memory_id)

            if memory is None:
                return False

            session.delete(memory)

            return True

    def count(self) -> int:
        """
        Devuelve el número total de recuerdos.
        """

        with get_session() as session:
            return session.query(Memory).count()