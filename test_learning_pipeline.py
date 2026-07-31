from app.learning.service import LearningService
from app.memory.repositories.memory_repository import MemoryRepository

learning = LearningService()

learning.learn(
    "Mi película favorita es Interstellar."
)

repo = MemoryRepository()

print()

print("Cantidad de recuerdos:")

print(repo.count())

print()

print("Últimos recuerdos:")

for memory in repo.get_recent(3):
    print(memory)