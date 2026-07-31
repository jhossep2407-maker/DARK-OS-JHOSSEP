from app.memory.extractors.memory_extractor import MemoryExtractor

extractor = MemoryExtractor()

examples = [
    "Mi color favorito es azul.",
    "Estoy creando DARK OS.",
    "Quiero aprender japonés.",
    "Mañana tengo examen.",
    "La Tierra gira alrededor del Sol.",
]

for text in examples:
    category = extractor.detect_category(text)

    print(f"{category.value:12} -> {text}")