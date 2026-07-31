"""
DARK OS
Dynamic Model Registry
"""

from __future__ import annotations

from google import genai

from app.core.config import settings

from app.ai.models.model_info import ModelInfo


class DynamicModelRegistry:

    def __init__(self) -> None:

        self.client = genai.Client(
            api_key=settings.ai.api_key,
        )

        self._models: list[ModelInfo] = []

        self.refresh()

    def refresh(self) -> None:

        self._models.clear()

        priority = 1

        preferred = [

            "models/gemini-3.1-flash-lite",

        ]

        available = {
            model.name: model
            for model in self.client.models.list()
        }

        for name in preferred:

            if name not in available:
                continue

            model = available[name]

            self._models.append(

                ModelInfo(

                    provider="gemini",

                    name=model.name,

                    priority=priority,

                    enabled=True,

                    context_window=getattr(
                        model,
                        "input_token_limit",
                        0,
                    ),

                )

            )

            priority += 1

    def models(self) -> list[ModelInfo]:

        return self._models