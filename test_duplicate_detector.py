from app.memory.dedup.duplicate_detector import DuplicateDetector

detector = DuplicateDetector()

print(
    detector.exists(
        "Comida favorita",
        "Pizza",
    )
)