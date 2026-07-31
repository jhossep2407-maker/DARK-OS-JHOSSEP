from app.memory.search.search_engine import MemorySearchEngine

engine = MemorySearchEngine()

questions = [
    "¿Cuál es mi color favorito?",
    "¿Qué lenguaje me gusta?",
    "¿En qué proyecto estoy trabajando?",
]

for question in questions:

    print("=" * 60)
    print(question)

    memories = engine.search(question)

    if not memories:
        print("Sin resultados.")
        continue

    for memory in memories:
        print(memory)