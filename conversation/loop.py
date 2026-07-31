"""
DARK OS
Conversation Loop
"""

from __future__ import annotations

import time

from app.audio.audio_manager import AudioManager
from app.conversation.service import ConversationService


class ConversationLoop:

    def __init__(self):

        self.audio = AudioManager()
        self.dark = ConversationService()

    def run(self):

        print("=" * 60)
        print("DARK iniciado.")
        print("Di 'salir' para terminar.")
        print("=" * 60)

        while True:

            try:

                message = self.audio.listen()

                if not message:
                    continue

                print(f"\n👤 Tú: {message}")

                if message.lower() in (
                    "salir",
                    "adiós",
                    "terminar",
                    "duerme",
                ):

                    self.audio.speak(
                        "Hasta luego."
                    )

                    break

                print("\n🧠 Pensando...")

                start = time.perf_counter()

                response = self.dark.chat(
                    message,
                )

                end = time.perf_counter()

                print(f"⏱ IA: {end-start:.2f}s")

                print(f"\n🤖 DARK: {response}")

                self.audio.speak(
                    response,
                )

            except KeyboardInterrupt:

                print("\nDARK detenido.")
                break

            except Exception as error:

                print(error)