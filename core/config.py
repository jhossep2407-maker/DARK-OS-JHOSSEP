"""
DARK OS
Configuration Manager

Este módulo centraliza toda la configuración del sistema.

Lee:

- .env (secretos)
- config/settings.toml (configuración)

Todo el proyecto deberá obtener la configuración desde aquí.
"""

from __future__ import annotations

import os
import tomllib
from pathlib import Path
from dataclasses import dataclass

from dotenv import load_dotenv

# -------------------------------------------------------
# Rutas
# -------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[2]

ENV_FILE = ROOT_DIR / ".env"

CONFIG_FILE = ROOT_DIR / "config" / "settings.toml"

# -------------------------------------------------------
# Cargar variables sensibles
# -------------------------------------------------------

load_dotenv(ENV_FILE)

# -------------------------------------------------------
# Leer configuración TOML
# -------------------------------------------------------

with open(CONFIG_FILE, "rb") as f:
    CONFIG = tomllib.load(f)


# =======================================================
# APP
# =======================================================

@dataclass(frozen=True)
class AppConfig:

    name: str

    version: str

    environment: str

    debug: bool


# =======================================================
# AI
# =======================================================

@dataclass(frozen=True)
class AIConfig:

    provider: str

    model: str

    temperature: float

    top_p: float

    max_tokens: int

    api_key: str


# =======================================================
# DATABASE
# =======================================================

@dataclass(frozen=True)
class DatabaseConfig:

    sqlite_path: Path

    vector_db_path: Path

    backup_path: Path


# =======================================================
# MEMORY
# =======================================================

@dataclass(frozen=True)
class MemoryConfig:

    short_memory_limit: int

    long_memory_limit: int

    summary_trigger: int

    vector_search_limit: int

    auto_save: bool

    auto_summarize: bool


# =======================================================
# VOICE
# =======================================================

@dataclass(frozen=True)
class VoiceConfig:

    provider: str

    language: str

    voice: str

    speed: float

    wake_word: str


# =======================================================
# SECURITY
# =======================================================

@dataclass(frozen=True)
class SecurityConfig:

    encryption: bool

    key_path: Path


# =======================================================
# DASHBOARD
# =======================================================

@dataclass(frozen=True)
class DashboardConfig:

    host: str

    port: int


# =======================================================
# PLUGINS
# =======================================================

@dataclass(frozen=True)
class PluginConfig:

    enabled: bool

    folder: Path


# =======================================================
# LOGGING
# =======================================================

@dataclass(frozen=True)
class LoggingConfig:

    level: str


# =======================================================
# SETTINGS
# =======================================================

class Settings:

    def __init__(self):

        self.app = AppConfig(**CONFIG["app"])

        self.ai = AIConfig(
            **CONFIG["ai"],
            api_key=os.getenv("OPENAI_API_KEY", "")
        )

        self.database = DatabaseConfig(
            sqlite_path=Path(CONFIG["database"]["sqlite_path"]),
            vector_db_path=Path(CONFIG["database"]["vector_db_path"]),
            backup_path=Path(CONFIG["database"]["backup_path"]),
        )

        self.memory = MemoryConfig(**CONFIG["memory"])

        self.voice = VoiceConfig(**CONFIG["voice"])

        self.security = SecurityConfig(
            encryption=CONFIG["security"]["encryption"],
            key_path=Path(CONFIG["security"]["key_path"]),
        )

        self.dashboard = DashboardConfig(**CONFIG["dashboard"])

        self.plugins = PluginConfig(
            enabled=CONFIG["plugins"]["enabled"],
            folder=Path(CONFIG["plugins"]["folder"]),
        )

        self.logging = LoggingConfig(**CONFIG["logging"])


settings = Settings()