"""
DARK OS
Test de Integración
"""

from app.conversation.service import ConversationService

conversation = ConversationService()

print("=" * 50)
print("PRIMER MENSAJE")
print("=" * 50)

response = conversation.chat(
    "Mi comida favorita es la pizza."
)

print(response)

print()
print("=" * 50)
print("SEGUNDO MENSAJE")
print("=" * 50)

response = conversation.chat(
    "¿Cuál es mi comida favorita?"
)

print(response)

print()
print("=" * 50)
print("TERCER MENSAJE")
print("=" * 50)

response = conversation.chat(
    "Estoy aprendiendo SQLAlchemy."
)

print(response)

print()
print("=" * 50)
print("CUARTO MENSAJE")
print("=" * 50)

response = conversation.chat(
    "¿Qué estoy aprendiendo?"
)

print(response)