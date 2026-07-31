"""
DARK OS
Model Selector Test
"""

from app.ai.models.model_selector import ModelSelector

selector = ModelSelector()

print("=" * 60)

model = selector.current("gemini")

print(model)

print("=" * 60)

while True:

    model = selector.next("gemini")

    if model is None:

        print("No quedan más modelos.")

        break

    print(model)