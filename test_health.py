from app.core.health import health

health.register("Config")
health.register("Logger")
health.register("Kernel")
health.register("Event Bus")
health.register("Module Loader")

if health.run():
    print("\nSistema listo.")
else:
    print("\nErrores encontrados.")