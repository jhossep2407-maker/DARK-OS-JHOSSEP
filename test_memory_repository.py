from app.memory.repositories.memory_repository import (
    MemoryRepository,
)

from app.memory.models import MemoryCategory

repo = MemoryRepository()

memory = repo.add_memory(
    category=MemoryCategory.PROJECT,
    title="Proyecto",
    content="Estoy creando DARK OS.",
    importance=10,
)

print(memory)

print("Memory guardada correctamente.")