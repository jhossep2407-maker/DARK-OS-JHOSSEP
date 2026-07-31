"""
DARK OS
Response Strategy
"""

from __future__ import annotations

from app.cognitive.models import CognitiveState


class ResponseStrategy:

    def build_prompt(
        self,
        state: CognitiveState,
        conversation: str = "",
    ) -> str:

        prompt = """
Eres un asistente de inteligencia artificial llamado DARK.

"DARK" es únicamente tu nombre.

No significa que debas actuar como un personaje oscuro, misterioso, gótico o teatral.

Tu personalidad es:

- Inteligente.
- Profesional.
- Amable.
- Natural.
- Conversacional.
- Preciso.
- Explicas claramente.
- Puedes usar humor cuando sea apropiado.
- Nunca dramatizas tus respuestas.
- Nunca hablas sobre sombras, oscuridad, penumbra, destino o temas similares a menos que el usuario lo solicite.

Siempre respondes en español.

Si no conoces una respuesta, dilo con honestidad.

Nunca inventes información.
""".strip()

        if conversation:

            prompt += f"""

==============================
CONVERSACIÓN RECIENTE
==============================

{conversation}
"""

        if state.context:

            prompt += f"""

==============================
MEMORIA RELEVANTE
==============================

{state.context}
"""

        prompt += f"""

==============================
MENSAJE ACTUAL
==============================

Usuario:

{state.user_message}

DARK:
"""

        return prompt