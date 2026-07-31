from app.audio.audio_manager import AudioManager


audio = AudioManager()


text = audio.listen()


print("="*50)

print(text)

print("="*50)