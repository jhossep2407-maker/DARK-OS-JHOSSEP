from app.core.module_loader import module_loader


class FakeModule:

    def initialize(self):
        print("Fake Module iniciado")


module_loader.register("fake", FakeModule())

module_loader.initialize_all()