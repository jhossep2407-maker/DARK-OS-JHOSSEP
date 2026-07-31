from piper.voice import PiperVoice
import inspect

print("=" * 80)
print("VERSIÓN DE LA API")
print("=" * 80)

print(inspect.signature(PiperVoice.load))

print()

print(inspect.signature(PiperVoice.synthesize))