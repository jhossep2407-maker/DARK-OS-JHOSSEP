from app.memory.repositories.memory_repository import MemoryRepository

repo = MemoryRepository()

print("=" * 70)
print("TODOS LOS RECUERDOS")
print("=" * 70)

memories = repo.get_recent(100)

for memory in reversed(memories):
    print(f"""
ID: {memory.id}
Categoría: {memory.category}
Título: {memory.title}
Contenido: {memory.content}
Importancia: {memory.importance}
""")