"""
DARK OS
Learning Service
"""

from __future__ import annotations

from app.learning.pipeline import LearningPipeline


class LearningService:
    """
    Servicio principal del sistema de aprendizaje.
    """

    def __init__(self) -> None:

        self.pipeline = LearningPipeline()

    def learn(
        self,
        text: str,
    ) -> None:
        """
        Aprende a partir de un texto.
        """

        self.pipeline.process(text)