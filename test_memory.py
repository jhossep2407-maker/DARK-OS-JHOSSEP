"""
DARK OS
Memory Inspector
"""

from app.memory.search.search_engine import MemorySearchEngine

engine = MemorySearchEngine()

print("=" * 70)
print("MEMORIA DE DARK")
print("=" * 70)

memories = engine.search("")

if not memories:

    print("No hay recuerdos.")

else:

    for i, memory in enumerate(memories, start=1):

        print(f"\n[{i}]")

        print(f"Categoría : {memory.category.value}")
        print(f"Título    : {memory.title}")
        print(f"Contenido : {memory.content}")
        print(f"Importancia : {memory.importance}")

print("\nTotal:", len(memories))