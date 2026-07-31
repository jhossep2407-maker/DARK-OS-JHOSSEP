from app.conversation.service import ConversationService

conversation = ConversationService()

response = conversation.chat(
    "Mi lenguaje favorito es Python."
)

print()
print(response)