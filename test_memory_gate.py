from app.context.memory_gate import MemoryGate

gate = MemoryGate()

tests = [

    "Hola",

    "Buenos días",

    "Gracias",

    "¿Cómo estás?",

    "¿Cuál es mi comida favorita?",

    "¿Qué recuerdas de mí?",

    "¿En qué proyecto estoy trabajando?",

    "Recuérdame mis objetivos.",

]

for text in tests:

    print("-" * 60)
    print(text)
    print(gate.should_search(text))