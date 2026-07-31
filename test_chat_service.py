from app.ai.chat_service import ChatService

chat = ChatService()

response = chat.chat(
    "Responde únicamente: ChatService funcionando."
)

print(response)