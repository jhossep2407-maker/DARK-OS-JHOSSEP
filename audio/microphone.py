"""
DARK OS
Microphone
"""

from __future__ import annotations

import sounddevice as sd

from scipy.io.wavfile import write


class Microphone:

    def record(
        self,
        filename: str = "input.wav",
        duration: int = 5,
        sample_rate: int = 16000,
    ) -> str:

        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16",
        )

        sd.wait()

        write(
            filename,
            sample_rate,
            audio,
        )

        return filename