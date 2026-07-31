"""
DARK OS

Gemini Fallback Test
"""

from app.ai.providers.gemini_provider import (
    GeminiProvider,
)

provider = GeminiProvider()

print("=" * 70)

response = provider.chat(
    "Responde únicamente: OK"
)

print()

print("=" * 70)

print(response)