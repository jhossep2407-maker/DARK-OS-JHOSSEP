from app.ai.orchestrator import AIOrchestrator

orchestrator = AIOrchestrator()

response = orchestrator.process(
    "¿Qué sabes de mí?"
)

print()
print(response)