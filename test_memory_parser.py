import json

from app.memory.ai.parser import MemoryAIParser

parser = MemoryAIParser()

fake_json = json.dumps(
    {
        "remember": True,
        "category": "preference",
        "title": "Comida favorita",
        "content": "Pizza",
        "importance": 8,
    }
)

memory = parser.parse(fake_json)

print(memory)