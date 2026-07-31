from app.memory.repositories.memory_repository import MemoryRepository

repo = MemoryRepository()

print("Total de recuerdos:", repo.count())