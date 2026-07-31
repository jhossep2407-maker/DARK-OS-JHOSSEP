"""
DARK OS
Gemini Speech To Text
"""

from __future__ import annotations

import time

from google import genai

from app.core.config import settings


class SpeechToText:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.ai.api_key,
        )

    def transcribe(
        self,
        audio_file: str,
    ) -> str:

        print("📤 Subiendo audio...")

        t0 = time.perf_counter()

        file = self.client.files.upload(
            file=audio_file,
        )

        print(
            f"Upload: {time.perf_counter()-t0:.2f}s"
        )

        print("🧠 Transcribiendo...")

        t0 = time.perf_counter()

        response = self.client.models.generate_content(
            model="models/gemini-flash-lite-latest",
            contents=[
                file,
                """
Transcribe exactamente el audio.
Devuelve solamente el texto.
Idioma: español.
"""
            ],
        )

        print(
            f"STT: {time.perf_counter()-t0:.2f}s"
        )

        return response.text.strip()