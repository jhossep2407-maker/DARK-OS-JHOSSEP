from app.memory.extractors.memory_extractor import MemoryExtractor

extractor = MemoryExtractor()

examples = [
    "Mi color favorito es azul.",
    "Mi comida favorita es la pizza.",
    "Mi lenguaje favorito es Python.",
    "Estoy creando DARK OS.",
    "Estoy aprendiendo SQLAlchemy.",
]

for text in examples:

    memory = extractor.extract(text)

    print("=" * 60)
    print(text)
    print("Categoría :", memory.category)
    print("Título    :", memory.title)
    print("Contenido :", memory.content)