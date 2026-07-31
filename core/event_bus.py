"""
DARK OS
Event Bus
"""

from __future__ import annotations

from collections import defaultdict
from typing import Callable

from app.core.events import Event
from app.core.logger import logger


EventHandler = Callable[[Event], None]


class EventBus:
    """
    Bus de eventos interno.
    """

    def __init__(self) -> None:
        self._listeners: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        """
        Registrar un evento.
        """
        self._listeners[event_name].append(handler)

        logger.info(f"Subscribed -> {event_name}")

    def publish(self, event: Event) -> None:
        """
        Publicar un evento.
        """

        logger.info(f"Event -> {event.name}")

        for handler in self._listeners[event.name]:
            handler(event)


event_bus = EventBus()