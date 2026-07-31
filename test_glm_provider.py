from app.ai.providers.glm_provider import GLMProvider

provider = GLMProvider()

response = provider.chat(
    "Responde únicamente con: Hola Jhossep."
)

print(response)