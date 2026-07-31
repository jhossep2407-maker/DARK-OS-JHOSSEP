from app.memory.utils.importance import ImportanceEngine

engine = ImportanceEngine()

examples = [
    "Hola",
    "Mi nombre es Jhossep.",
    "Estoy creando DARK OS.",
    "Recuerda que mi color favorito es azul.",
]

for text in examples:
    score = engine.calculate(text)

    print(f"{score}/10 -> {text}")