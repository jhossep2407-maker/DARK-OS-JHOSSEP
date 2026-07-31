from app.ai.prompts.builder import PromptBuilder

builder = PromptBuilder()

prompt = builder.build(
    "¿Cómo me llamo?"
)

print(prompt)