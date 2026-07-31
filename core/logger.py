"""
DARK OS
Professional Logger

Sistema centralizado de registros.
"""

from __future__ import annotations

import logging
from pathlib import Path

from app.core.config import settings

# ==========================================================
# Crear carpeta de logs automáticamente
# ==========================================================

LOG_FOLDER = Path("data/logs")
LOG_FOLDER.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_FOLDER / "dark.log"

# ==========================================================
# Configuración del logger
# ==========================================================

logging.basicConfig(
    level=getattr(logging, settings.logging.level.upper()),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
    force=True,
)

# ==========================================================
# Logger principal de DARK
# ==========================================================

logger = logging.getLogger("DARK")