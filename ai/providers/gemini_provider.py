"""
DARK OS
Gemini Provider
"""

from __future__ import annotations

from google import genai
from google.genai.errors import ClientError

from app.core.config import settings

from app.ai.models.model_manager import (
    model_manager,
)


class GeminiProvider:
    """
    Proveedor de Google Gemini.

    Cambia automáticamente de modelo cuando uno
    agota su cuota o deja de estar disponible.
    """

    def __init__(self) -> None:

        self.client = genai.Client(
            api_key=settings.ai.api_key,
        )

        self.selector = model_manager.selector

    def chat(
        self,
        message: str,
    ) -> str:
        """
        Envía un mensaje al modelo Gemini disponible.
        """

        while True:

            model = self.selector.current()

            print(
                f"[Gemini] Usando: {model.name}"
            )

            try:

                response = self.client.models.generate_content(
                    model=model.name,
                    contents=message,
                )

                #
                # Caso normal
                #

                if (
                    hasattr(response, "text")
                    and response.text
                ):
                    return response.text

                #
                # Algunos modelos devuelven la respuesta
                # dentro de candidates.
                #

                if (
                    hasattr(response, "candidates")
                    and response.candidates
                ):

                    parts = []

                    candidate = response.candidates[0]

                    if (
                        hasattr(candidate, "content")
                        and candidate.content
                        and hasattr(candidate.content, "parts")
                    ):

                        for part in candidate.content.parts:

                            if (
                                hasattr(part, "text")
                                and part.text
                            ):
                                parts.append(
                                    part.text
                                )

                    if parts:
                        return "".join(parts)

                #
                # Nunca devolver None
                #

                return (
                    "Lo siento, no pude generar "
                    "una respuesta."
                )

            except ClientError as error:

                error_text = str(error)

                #
                # Cuota agotada
                #

                if (
                    "429" in error_text
                    or
                    "RESOURCE_EXHAUSTED" in error_text
                ):

                    print(
                        f"[Gemini] Cuota agotada: {model.name}"
                    )

                    if self.selector.next() is None:

                        raise RuntimeError(
                            "Todos los modelos Gemini "
                            "agotaron su cuota."
                        )

                    continue

                #
                # Modelo inexistente
                #

                if (
                    "404" in error_text
                    or
                    "NOT_FOUND" in error_text
                ):

                    print(
                        f"[Gemini] Modelo inexistente: {model.name}"
                    )

                    if self.selector.next() is None:

                        raise RuntimeError(
                            "No existe ningún modelo "
                            "Gemini válido."
                        )

                    continue

                #
                # Error temporal del servidor
                #

                if (
                    "Server disconnected"
                    in error_text
                ):

                    print(
                        "[Gemini] Reconectando..."
                    )

                    continue

                #
                # Otros errores
                #

                raise

            except Exception as error:

                print(
                    f"[Gemini] Error: {error}"
                )

                return (
                    "Lo siento, ocurrió un error "
                    "al generar la respuesta."
                )