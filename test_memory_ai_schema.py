from app.memory.ai.schemas import AIMemoryResult
from app.memory.models import MemoryCategory


memory = AIMemoryResult(
    remember=True,
    category=MemoryCategory.PREFERENCE,
    title="Color favorito",
    content="Azul",
    importance=8,
)


print(memory)