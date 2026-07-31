from app.ai.router import AIRouter

router = AIRouter()

response = router.provider.chat(
    "Responde únicamente: Router funcionando."
)

print(response)