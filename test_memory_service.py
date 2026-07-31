from app.memory.services.memory_service import MemoryService
from app.memory.models import ConversationRole

memory = MemoryService()

message = memory.process_message(
    role=ConversationRole.USER,
    content="Hola DARK, esta es mi primera memoria.",
)

print(message)

print("Memory Service funcionando correctamente.")