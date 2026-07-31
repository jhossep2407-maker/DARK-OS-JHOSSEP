"""
DARK OS
Prompt Builder + Memory Gate Test
"""

from app.ai.prompts.builder import PromptBuilder

builder = PromptBuilder()

print("=" * 70)
print("HOLA")
print("=" * 70)

print(
    builder.build(
        "Hola"
    )
)

print()

print("=" * 70)
print("MEMORIA")
print("=" * 70)

print(
    builder.build(
        "¿Cuál es mi videojuego favorito?"
    )
)