from app.memory.repositories.conversation_repository import (
    ConversationRepository,
)
from app.memory.models import ConversationRole

repo = ConversationRepository()

# Crear dos mensajes
m1 = repo.add_message(
    role=ConversationRole.USER,
    content="Mensaje 1",
)

m2 = repo.add_message(
    role=ConversationRole.USER,
    content="Mensaje 2",
)

print("Antes:", repo.count())

# Eliminar uno
deleted = repo.delete_by_id(m1.id)

print("Eliminado:", deleted)
print("Después:", repo.count())

# Eliminar todo
total = repo.delete_all()

print("Registros eliminados:", total)
print("Total final:", repo.count())