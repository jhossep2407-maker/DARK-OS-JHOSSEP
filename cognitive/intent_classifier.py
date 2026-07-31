"""
DARK OS
Intent Classifier
"""

from __future__ import annotations


class IntentClassifier:

    def classify(
        self,
        message: str,
    ) -> str:

        text = message.lower()

        if any(word in text for word in (
            "recuerda",
            "favorito",
            "qué sabes",
            "que sabes",
        )):
            return "memory"

        if any(word in text for word in (
            "crea",
            "haz",
            "genera",
        )):
            return "task"

        return "conversation"