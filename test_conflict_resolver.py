from app.memory.models import Memory, MemoryCategory
from app.memory.resolver.conflict_resolver import MemoryConflictResolver

resolver = MemoryConflictResolver()

memory = Memory(
    category=MemoryCategory.PREFERENCE,
    title="Color favorito",
    content="Azul",
    importance=7,
)

print(resolver.resolve(memory))