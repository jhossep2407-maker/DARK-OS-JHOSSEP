from app.memory.database import get_session

with get_session() as session:
    print("Sesión creada correctamente.")
    print(type(session))