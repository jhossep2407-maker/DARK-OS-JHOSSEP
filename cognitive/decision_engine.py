"""
DARK OS
Decision Engine
"""

from __future__ import annotations

from app.cognitive.models import CognitiveState


class DecisionEngine:

    def decide(
        self,
        state: CognitiveState,
    ) -> CognitiveState:

        state.use_memory = (
            state.intent == "memory"
        )

        state.use_tools = (
            state.intent == "task"
        )

        return state