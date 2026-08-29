from .job import Job

# Base class for the Character
class Character():
    id: int
    name: str    
    world: str # TODO: pending world thinking
    jobs: list[Job]
    mounts: int # TODO: class Mount creation
    minions: int # TODO: class Minions creation
    achievements: int

    def __init__(self, id, name, world, mounts, minions, achievements):
        self.id = id
        self.name = name
        self.world = world
        self.mounts = mounts
        self.minions = minions
        self.achievements = achievements
