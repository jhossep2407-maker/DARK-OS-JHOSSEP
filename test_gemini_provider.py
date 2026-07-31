from app.ai.providers.gemini_provider import GeminiProvider

provider = GeminiProvider()

response = provider.chat(
    "Responde únicamente: Hola DARK."
)

print(response)