from app.memory.pipeline.normalizer import MemoryNormalizer

normalizer = MemoryNormalizer()

examples = [
    "Azul.",
    "La pizza.",
    "python.",
    "sqlalchemy.",
    "   hola mundo.   ",
    "Los videojuegos.",
]

for text in examples:

    print("=" * 60)
    print("Original   :", repr(text))
    print("Normalizado:", repr(normalizer.normalize(text)))