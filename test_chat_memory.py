from app.ai.chat_service import ChatService

chat = ChatService()

response = chat.chat(
    "¿Qué sabes de mí?"
)

print()

print(response)