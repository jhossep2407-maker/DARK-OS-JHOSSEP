"""
DARK OS
Memory AI
"""

from __future__ import annotations

from app.ai.providers.gemini_provider import GeminiProvider
from app.memory.ai.parser import MemoryAIParser
from app.memory.ai.schemas import MemoryAIResult


class MemoryAI:
    """
    Utiliza IA para decidir qué información
    merece convertirse en un recuerdo permanente.
    """

    def __init__(self) -> None:

        self.ai = GeminiProvider()
        self.parser = MemoryAIParser()

    def analyze(
        self,
        text: str,
    ) -> MemoryAIResult:

        prompt = f"""
Eres el módulo de memoria permanente de DARK.

NO eres un asistente.

NO conversas.

NO respondes preguntas.

Tu única función es analizar el mensaje del usuario y devolver ÚNICAMENTE un objeto JSON válido.

Solo recuerda información útil para futuras conversaciones.



Recuerda:

- Preferencias
- Gustos
- Objetivos
- Proyectos
- Información personal estable
- Habilidades
- Información que el usuario considere importante
- Logros
- Si el usuario te dice que recuerdes algo, recuerda eso

No recuerdes:

- Saludos
- Despedidas
- Conversación casual
- Preguntas
- Chistes
- Respuestas del asistente
- Estados temporales

Si NO debe recordarse:

{{
    "remember": false,
    "category": "fact",
    "title": "",
    "content": "",
    "importance": 0
}}

Si SÍ debe recordarse:

{{
    "remember": true,
    "category": "preference",
    "title": "...",
    "content": "...",
    "importance": 8
}}

REGLAS:

- Devuelve únicamente JSON.
- No uses Markdown.
- No uses ```json.
- No escribas explicaciones.
- el contenido no idebe incliur información de contexto, solo el contenido del recuerdo. No digas por ejemplo: Me gusta el color azul, sino Azul.

Mensaje:

{text}
"""

        response = self.ai.chat(prompt)

        print("\n========== RESPUESTA DE GEMINI ==========\n")
        print(response)
        print("\n=========================================\n")

        return self.parser.parse(response)