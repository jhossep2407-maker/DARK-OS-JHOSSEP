from app.core.container import container

response = container.ai.chat(
    "Responde únicamente: Container AI funcionando."
)

print(response)