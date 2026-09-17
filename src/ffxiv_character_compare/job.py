class Job():
    name: str
    level: int

    def __init__(self, name: str, level: int):
        self.name: str = name
        self.level: int = level

    def __eq__(self, other: Job) -> bool:
        return self.level == other.level

    def __lt__(self, other: Job) -> bool:
        return self.level < other.level

    def __gt__(self, other: Job) -> bool:
        return self.level > other.level
