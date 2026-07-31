"""
DARK OS

Global Model Manager Test
"""

from app.ai.models.model_manager import (
    model_manager,
)


selector1 = model_manager.selector

selector2 = model_manager.selector


print(
    selector1 is selector2
)


print(
    selector1.current(
        "gemini"
    )
)