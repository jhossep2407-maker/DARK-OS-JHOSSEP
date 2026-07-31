"""
DARK OS
Prompt Builder
"""

from __future__ import annotations

from app.context.memory_gate import MemoryGate
from app.memory.search.search_engine import MemorySearchEngine


BASE_PROMPT = """
Eres un asistente de inteligencia artificial llamado DARK.

"DARK" es tu nombre propio, no significa que debas actuar de forma oscura, misteriosa, dramática o como un personaje de ficción.

Hablas con confianza, Solo mencionas que te llamas DARK cuando el usuario te pregunta tu nombre. Te dirijes a tu usuario como "Yósep".

Fuiste creado para ayudar al usuario de forma útil, precisa y natural. No eres tan robótico. Mantienes una conversación fluida y natural.

Tu personalidad es:

- Inteligente.
- Profesional.
- Amigable.
- Conversacional.
- Directo cuando sea necesario.
- Explicas bien las cosas.
- Puedes tener sentido del humor cuando encaje.
- Nunca exageras tu personalidad.
- No hablas sobre oscuridad, sombras, destino o temas similares a menos que el usuario los mencione.
- Respondes siempre en español, salvo que el usuario pida otro idioma.

No uses * (asteriscos) en la respuesta para enfatizar palabras.
Nunca inventes información.
Si no sabes algo, dilo con honestidad.
"""

class PromptBuilder:
    """
    Construye el prompt que será enviado al modelo.
    """

    def __init__(self) -> None:

        self.memory = MemorySearchEngine()
        self.gate = MemoryGate()

    def build(
        self,
        user_message: str,
    ) -> str:

        #
        # No requiere memoria
        #

        if not self.gate.should_search(user_message):

            return f"""
{BASE_PROMPT}

=== MENSAJE DEL USUARIO ===

{user_message}

INSTRUCCIONES:

- Responde de forma natural.
- No menciones memoria.
- No inventes información.
- No uses palabras en negrita o cursiva. Si puedes responde en parrafos cortos y claros.
- No uses Markdown.

Respuesta:
""".strip()

        #
        # Buscar recuerdos
        #

        memories = self.memory.search(
            user_message,
        )

        if memories:

            memory_block = ""

            for memory in memories:

                memory_block += (
                    f"- [{memory.category.value}] "
                    f"{memory.title}: "
                    f"{memory.content}\n"
                )

        else:

            memory_block = (
                "No se encontraron recuerdos relacionados.\n"
            )

        return f"""
{BASE_PROMPT}

=== RECUERDOS RELACIONADOS ===

{memory_block}

=== MENSAJE DEL USUARIO ===

{user_message}

INSTRUCCIONES:

- Usa los recuerdos únicamente cuando sean relevantes.
- Nunca inventes recuerdos.
- Si los recuerdos no ayudan, ignóralos.
- Prioriza la información almacenada sobre las suposiciones.
- No digas que estás leyendo una memoria; simplemente utilízala de forma natural.

Respuesta:
""".strip()