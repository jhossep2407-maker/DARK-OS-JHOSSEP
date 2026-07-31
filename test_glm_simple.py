from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    api_key=settings.ai.api_key,
    base_url="https://api.z.ai/api/paas/v4/",
)

response = client.chat.completions.create(
    model="glm-5",
    messages=[
        {
            "role": "user",
            "content": "Responde únicamente con: Hola DARK",
        }
    ],
)

print(response.choices[0].message.content)