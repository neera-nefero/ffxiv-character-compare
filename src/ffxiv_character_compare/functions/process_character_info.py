import json
from datetime import datetime
from pathlib import Path

from .get_online_character import get_job_info, get_minion_info, get_mount_info, get_achievement_info
from .process_character_jobs import process_character_jobs
from .process_character_minions import process_character_minions
from .process_character_mounts import process_character_mounts
from .process_character_achievements import process_character_achievements
from ..constants import NEERA_ID

def generate_chatacter_cache(chr_name: str, chr_id: int) -> None:
    cache_path = Path(f"data/cache/characters/{chr_id}.json")
    cache_path.parent.mkdir(parents=True, exist_ok=True)

    json_content = {
        "name": chr_name,
        "updated_at": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        "jobs": process_character_jobs(get_job_info(chr_id)),
        "minions": process_character_minions(get_minion_info(chr_id)),
        "mounts": process_character_mounts(get_mount_info(chr_id)),
        "achievement_points": process_character_achievements(get_achievement_info(chr_id)),
    }

    with cache_path.open("w", encoding="utf-8") as file:
        json.dump(json_content, file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    #generate_chatacter_cache("Neera Nefero", 14246687)
    #generate_chatacter_cache("No Achievements", 37322600)
    #generate_chatacter_cache("No Mounts", 41559449)
    pass