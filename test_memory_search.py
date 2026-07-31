from app.memory.search.search_engine import MemorySearchEngine

engine = MemorySearchEngine()

memories = engine.get_recent()

print()

print("Recuerdos encontrados:")

for memory in memories:
    print(memory)