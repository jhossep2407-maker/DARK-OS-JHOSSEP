from app.cognitive.core import CognitiveCore

core = CognitiveCore()

print("=" * 70)
print(core.process("Hola"))

print()

print("=" * 70)
print(core.process("¿Cuál es mi videojuego favorito?"))