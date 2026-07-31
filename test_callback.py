import sounddevice as sd

print(sd.default.device)

sd.default.device = (
    None,
    14,
)

print(sd.default.device)