"""
DARK OS
Complete Memory Flow Test
"""

from app.conversation.service import ConversationService

service = ConversationService()

print("=" * 70)
print("PRIMER MENSAJE")
print("=" * 70)

print(
    service.chat(
        "Mi videojuego favorito es Minecraft."
    )
)

print()

print("=" * 70)
print("SEGUNDO MENSAJE")
print("=" * 70)

print(
    service.chat(
        "¿Cuál es mi videojuego favorito?"
    )
)