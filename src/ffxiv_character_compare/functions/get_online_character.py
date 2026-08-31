# Gets online info from the selected character

import requests

from ..constants import LODESTONE_CHARACTER_BASE_URL, LODESTONE_JOB_PATH, LODESTONE_MINION_PATH, LODESTONE_MOUNT_PATH, LODESTONE_ACHIEVEMENT_PATH, LODESTONE_PHYSICAL_DC_FILTER_PREFIX, LODESTONE_LOGICAL_DC_FILTER_PREFIX, LODESTONE_WORLD_FILTER_PREFIX

def search_character(chr_name: str, world: str | None) -> str:
    pass

def get_job_info(chr_id: int) -> str:
    pass

def get_minions_info(chr_id: int) -> str:
    pass

def get_mounts_info(chr_id: int) -> str:
    pass

def get_achievements_info(chr_id: int) -> str:
    pass