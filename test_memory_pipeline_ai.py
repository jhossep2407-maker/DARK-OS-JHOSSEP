from app.memory.pipeline.memory_pipeline import MemoryPipeline
from app.memory.models import ConversationRole

pipeline = MemoryPipeline()

pipeline.run(
    ConversationRole.USER,
    "Mi videojuego favorito es Minecraft."
)

print("OK")