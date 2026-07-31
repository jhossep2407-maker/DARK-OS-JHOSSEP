from app.core.event_bus import event_bus
from app.core.events import Event


def on_message(event: Event):
    print("Evento recibido:")
    print(event.name)
    print(event.data)


event_bus.subscribe("message", on_message)

event_bus.publish(
    Event(
        name="message",
        data={
            "text": "Hola DARK"
        }
    )
)