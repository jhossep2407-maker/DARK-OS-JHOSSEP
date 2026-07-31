"""
DARK OS
Database

Gestiona la conexión con SQLite mediante SQLAlchemy.
"""

from __future__ import annotations

from pathlib import Path
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


# ==========================================================
# Ruta de la base de datos
# ==========================================================

DATABASE_DIR = Path("data/database")
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "dark.db"

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

# ==========================================================
# Engine
# ==========================================================

engine = create_engine(
    DATABASE_URL,
    echo=False,
)

# ==========================================================
# Session Factory
# ==========================================================

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

# ==========================================================
# Session Manager
# ==========================================================

@contextmanager
def get_session() -> Session: # type: ignore
    """
    Proporciona una sesión segura de SQLAlchemy.

    Hace commit automáticamente si todo sale bien,
    rollback si ocurre un error y siempre cierra
    la conexión al finalizar.
    """

    session = SessionLocal()

    try:
        yield session
        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()

from contextlib import contextmanager
from sqlalchemy.orm import Session

# ==========================================================
# Base
# ==========================================================

from app.memory.models import Base

def create_database() -> None:
    """
    Crea automáticamente todas las tablas definidas
    en models.py.
    """

Base.metadata.create_all(bind=engine)