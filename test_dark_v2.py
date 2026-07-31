"""
DARK OS V2
"""

from app.conversation.service import ConversationService

dark = ConversationService()

tests = [

    "Hola",

    "Mi color favorito es negro.",

    "¿Cuál es mi color favorito?",

    "Estoy creando un sistema operativo con IA.",

    "¿En qué proyecto estoy trabajando?",

]

for message in tests:

    print("=" * 70)
    print("USUARIO")
    print(message)
    print()

    response = dark.chat(
        message,
    )

    print("DARK")
    print(response)
    print()