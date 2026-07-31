"""
DARK OS
Text To Speech
"""

from __future__ import annotations

import time
import numpy as np
import sounddevice as sd

from pathlib import Path
from piper.voice import PiperVoice


class TextToSpeech:

    def __init__(self):

        self.voice = PiperVoice.load(
            Path("models/piper/es.onnx"),
        )

    def speak(
        self,
        text: str,
    ):

        audio = []

        sample_rate = None

        for chunk in self.voice.synthesize(text):

            sample_rate = chunk.sample_rate

            audio.append(
                chunk.audio_int16_array
            )

        if not audio:
            return

        samples = np.concatenate(audio)

        sd.play(
            samples,
            sample_rate,
            blocking=True,
        )

        sd.wait()

        time.sleep(0.15)