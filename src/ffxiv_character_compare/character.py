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

    def __init__(self, id, name, world, jobs, mounts, minions, achievements):
        self.id: int = id
        self.name: str = name
        self.world: str = world
        self.jobs: list[Job] = jobs
        self.mounts: int = mounts
        self.minions: int = minions
        self.achievements: int = achievements
