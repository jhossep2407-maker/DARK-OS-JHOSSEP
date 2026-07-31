"""
DARK OS
Model Selector
"""

from __future__ import annotations

from app.ai.models.dynamic_model_registry import (
    DynamicModelRegistry,
)


class ModelSelector:

    def __init__(self):

        self.registry = DynamicModelRegistry()

        self.index = 0

    def current(self):

        return self.registry.models()[self.index]

    def next(self):

        self.index += 1

        if self.index >= len(
            self.registry.models()
        ):
            return None

        return self.registry.models()[self.index]

    def reset(self):

        self.index = 0