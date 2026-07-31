from app.ai.models.model_manager import (
    model_manager,
)

print()

print("=" * 70)

for model in model_manager.selector.registry.models():

    print(model.name)

print("=" * 70)