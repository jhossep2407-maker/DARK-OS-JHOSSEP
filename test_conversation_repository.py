from app.memory.repositories.conversation_repository import (
    ConversationRepository,
)

from app.memory.models import ConversationRole

repo = ConversationRepository()

# Guardar mensaje
message = repo.add_message(
    role=ConversationRole.USER,
    content="Hola DARK",
)

print("Guardado:")
print(message)

# Recuperar mensaje
found = repo.get_by_id(message.id)

print("\nRecuperado:")
print(found)

assert found is not None
assert found.id == message.id
assert found.content == "Hola DARK"

print("\nPrueba superada.")

print("\nÚltimos mensajes:")

messages = repo.get_recent_messages(limit=5)

for msg in messages:
    print(msg)

print("\nCantidad total:")

print(repo.count())