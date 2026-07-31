"""
DARK OS
Model Manager
"""

from __future__ import annotations

from app.ai.models.model_selector import (
    ModelSelector,
)


class ModelManager:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.selector = (
                ModelSelector()
            )

        return cls._instance


model_manager = ModelManager()