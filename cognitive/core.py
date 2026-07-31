"""
DARK OS
Cognitive Core
"""

from __future__ import annotations

from app.cognitive.models import CognitiveState
from app.cognitive.intent_classifier import IntentClassifier
from app.cognitive.context_engine import ContextEngine
from app.cognitive.decision_engine import DecisionEngine
from app.cognitive.response_strategy import ResponseStrategy


class CognitiveCore:

    def __init__(self):

        self.intent = IntentClassifier()

        self.context = ContextEngine()

        self.decision = DecisionEngine()

        self.strategy = ResponseStrategy()

    def process(
        self,
        message: str,
        conversation: str = "",
    ) -> str:

        state = CognitiveState(
            user_message=message,
        )

        state.intent = self.intent.classify(
            message,
        )

        state = self.decision.decide(
            state,
        )

        if state.use_memory:

            state.context = self.context.build(
                message,
            )

        return self.strategy.build_prompt(
            state=state,
            conversation=conversation,
        )