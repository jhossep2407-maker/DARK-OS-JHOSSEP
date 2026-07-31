from app.memory.search.processor import QueryProcessor

processor = QueryProcessor()

examples = [
    "¿Cuál es mi comida favorita?",
    "¿Qué estoy aprendiendo?",
    "¿Cuál es mi color favorito?",
    "¿Qué sabes sobre DARK OS?",
    "¿En qué lenguaje programo?",
]

for example in examples:
    print(f"Entrada : {example}")
    print(f"Salida  : {processor.process(example)}")
    print()