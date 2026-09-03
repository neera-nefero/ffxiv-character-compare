# Gets online info from the selected character

import requests

from ..constants import LODESTONE_CHARACTER_BASE_URL, LODESTONE_JOB_PATH, LODESTONE_MINION_PATH, LODESTONE_MOUNT_PATH, LODESTONE_ACHIEVEMENT_PATH, LODESTONE_PHYSICAL_DC_FILTER_PREFIX, LODESTONE_LOGICAL_DC_FILTER_PREFIX, LODESTONE_WORLD_FILTER_PREFIX

def search_character(chr_name: str, world: str | None) -> str:
    pass

def get_job_info(chr_id: int) -> str:
    response = requests.get(f"{LODESTONE_CHARACTER_BASE_URL}/{chr_id}/{LODESTONE_JOB_PATH}/", timeout=10)
    response.raise_for_status()
    return response.text

def get_minion_info(chr_id: int) -> str:
    response = requests.get(f"{LODESTONE_CHARACTER_BASE_URL}/{chr_id}/{LODESTONE_MINION_PATH}/", timeout=10)
    response.raise_for_status()
    return response.text

def get_mount_info(chr_id: int) -> str:
    response = requests.get(f"{LODESTONE_CHARACTER_BASE_URL}/{chr_id}/{LODESTONE_MOUNT_PATH}/", timeout=10)
    response.raise_for_status()
    return response.text

def get_achievement_info(chr_id: int) -> str:
    response = requests.get(f"{LODESTONE_CHARACTER_BASE_URL}/{chr_id}/{LODESTONE_ACHIEVEMENT_PATH}/", timeout=10)
    response.raise_for_status()
    return response.text