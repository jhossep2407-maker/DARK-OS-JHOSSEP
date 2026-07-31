"""
DARK OS
GLM Provider
"""

from __future__ import annotations

from openai import OpenAI

from app.core.config import settings
from app.ai.providers.base import BaseAIProvider


class GLMProvider(BaseAIProvider):
    """
    Proveedor para los modelos GLM (Z.ai).
    """

    def __init__(self) -> None:

        self.client = OpenAI(
            api_key=settings.ai.api_key,
            base_url="https://api.z.ai/api/paas/v4/",
        )

    def chat(
        self,
        message: str,
    ) -> str:

        response = self.client.chat.completions.create(
            model=settings.ai.model,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            temperature=settings.ai.temperature,
            top_p=settings.ai.top_p,
            max_tokens=settings.ai.max_tokens,
        )

        return response.choices[0].message.content