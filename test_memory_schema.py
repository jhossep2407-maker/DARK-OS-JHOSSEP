from app.memory.ai.schemas import MemoryAIResult
from app.memory.models import MemoryCategory

result = MemoryAIResult(
    remember=True,
    category=MemoryCategory.PREFERENCE,
    title="Color favorito",
    content="Azul",
    importance=8,
)

print(result)