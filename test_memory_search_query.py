from app.memory.search.search_engine import MemorySearchEngine

engine = MemorySearchEngine()

memories = engine.search("Python")

print()

print("Resultados:")

for memory in memories:
    print(memory)