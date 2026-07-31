"""
DARK OS

Gemini Provider Test
"""

from app.ai.providers.gemini_provider import (
    GeminiProvider,
)

provider = GeminiProvider()

response = provider.chat(
    "Di solamente la palabra OK."
)

print(response)