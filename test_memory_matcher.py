from app.memory.matcher.matcher import MemoryMatcher
from app.memory.models import Memory, MemoryCategory

matcher = MemoryMatcher()

memory = Memory(
    category=MemoryCategory.PREFERENCE,
    title="Comida favorita",
    content="Pizza",
    importance=7,
)

match, score = matcher.find_best_match(memory)

print(match)
print(score)