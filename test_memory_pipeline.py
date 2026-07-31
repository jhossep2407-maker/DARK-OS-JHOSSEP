from app.memory.pipeline.memory_pipeline import MemoryPipeline
from app.memory.models import ConversationRole

pipeline = MemoryPipeline()

conversation = pipeline.run(
    role=ConversationRole.USER,
    content="Estoy creando DARK OS y quiero recordar este proyecto.",
)

print(conversation)

print("Memory Pipeline funcionando correctamente.")