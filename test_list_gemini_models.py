"""
DARK OS

Lista todos los modelos Gemini disponibles.
"""

from app.ai.providers.gemini_provider import GeminiProvider

provider = GeminiProvider()

client = provider.client

print("=" * 80)
print("MODELOS DISPONIBLES")
print("=" * 80)

for model in client.models.list():

    print(model.name)