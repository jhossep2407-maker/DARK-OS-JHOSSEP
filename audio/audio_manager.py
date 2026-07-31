"""
DARK OS
Audio Manager
"""

from __future__ import annotations

import time

from app.audio.microphone import Microphone
from app.audio.speech_to_text import SpeechToText
from app.audio.text_to_speech import TextToSpeech


class AudioManager:

    def __init__(self):

        self.microphone = Microphone()
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

    def listen(self):

        print("\n🎤 Escuchando...")

        start = time.perf_counter()

        audio = self.microphone.record()

        print("✅ Audio capturado")

        text = self.stt.transcribe(audio)

        end = time.perf_counter()

        print(f"⏱ STT: {end-start:.2f}s")

        return text

    def speak(
        self,
        text: str,
    ):

        start = time.perf_counter()

        self.tts.speak(text)

        end = time.perf_counter()

        print(f"⏱ TTS: {end-start:.2f}s")