from app.memory.services.memory_service import MemoryService
from app.memory.models import ConversationRole

memory = MemoryService()

memory.process_message(
    role=ConversationRole.USER,
    content="Recuerda que mi color favorito es azul.",
)

print("Proceso completado correctamente.")