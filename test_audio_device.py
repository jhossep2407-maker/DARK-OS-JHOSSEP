import sounddevice as sd

print("=" * 60)

print(sd.query_devices(14))

print("=" * 60)

print(sd.query_hostapis())