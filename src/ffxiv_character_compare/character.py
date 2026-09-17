from .job import Job

class Character():
    name: str    
    jobs: list[Job]
    mounts: int
    minions: int
    achievements: int

    def __init__(self, name, jobs, mounts, minions, achievements):
        self.name: str = name
        self.jobs: list[Job] = jobs
        self.mounts: int = mounts
        self.minions: int = minions
        self.achievements: int = achievements

    def compare_characters(self, other: Character) -> list[str]:
        compare_result: list[str] = []

        compare_result.append(f"{self.name} VS {other.name}")
        compare_result.append(self.compare_mounts(other))
        compare_result.append(self.compare_minions(other))
        compare_result.append(self.compare_achievements(other))
        compare_result.extend(self.compare_jobs(other))

        return compare_result

    def compare_jobs(self, other: Character) -> list[str]:        
        job_result: list[str] = []
        for i in range(0, len(self.jobs)):
            result = f"{self.name} wins with {self.jobs[i].level - other.jobs[i].level} more level"
            if (self.jobs[i] == other.jobs[i]):
                result = f"Tie result"
            if (self.jobs[i] < other.jobs[i]):
                result = f"{other.name} wins with {other.jobs[i].level - self.jobs[i].level} more level"
            job_result.append(f"{self.jobs[i].name} - lvl{self.jobs[i].level} vs lvl {other.jobs[i].level}: {result}")
        return job_result

    def compare_mounts(self, other: Character) -> str:
        result = f"{self.name} wins with {self.mounts - other.mounts} more mounts"
        if (self.mounts == other.mounts):
            result = f"Tie result"
        if (self.mounts < other.mounts):
            result = f"{other.name} wins with {other.mounts - self.mounts} more mounts"
        return f"{self.mounts} mounts vs {other.mounts}: {result}"
    def compare_minions(self, other: Character) -> str:
        result = f"{self.name} wins with {self.minions - other.minions} more minions"
        if (self.minions == other.minions):
            result = f"Tie result"
        if (self.minions < other.minions):
            result = f"{other.name} wins with {other.minions - self.minions} more minions"
        return f"{self.minions} minions vs {other.minions}: {result}"
    def compare_achievements(self, other: Character) -> str:
        result = f"{self.name} wins with {self.achievements - other.achievements} more achievements points"
        if (self.achievements == other.achievements):
            result = f"Tie result"
        if (self.achievements < other.achievements):
            result = f"{other.name} wins with {other.achievements - self.achievements} more achievements points"
        return f"{self.achievements} achievements points vs {other.achievements}: {result}"     