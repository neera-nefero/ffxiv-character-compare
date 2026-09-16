# Gets online info from the selected character

import requests
from http import HTTPStatus

from ...constants import LODESTONE_CHARACTER_BASE_URL, LODESTONE_JOB_PATH, LODESTONE_MINION_PATH, LODESTONE_MOUNT_PATH, LODESTONE_ACHIEVEMENT_PATH

def search_character(chr_name: str, world: str | None = None, world_prefix: str | None = None) -> str:
    print(f"Request to: {LODESTONE_CHARACTER_BASE_URL}/?q={chr_name.replace(" ", "+")}&worldname={world_prefix}{world}")
    response = requests.get(f"{LODESTONE_CHARACTER_BASE_URL}/?q={chr_name.replace(" ", "+")}&worldname={world_prefix}{world}", timeout=10)
    response.raise_for_status()
    return response.text

def get_job_info(chr_id: int) -> str:
    response = requests.get(f"{LODESTONE_CHARACTER_BASE_URL}/{chr_id}/{LODESTONE_JOB_PATH}/", timeout=10)
    response.raise_for_status()
    return response.text

def get_minion_info(chr_id: int) -> str | None:
    response = requests.get(f"{LODESTONE_CHARACTER_BASE_URL}/{chr_id}/{LODESTONE_MINION_PATH}/", timeout=10)
    if response.status_code == HTTPStatus.FORBIDDEN or response.status_code == HTTPStatus.NOT_FOUND:
        return None    
    response.raise_for_status()
    return response.text

def get_mount_info(chr_id: int) -> str | None:
    response = requests.get(f"{LODESTONE_CHARACTER_BASE_URL}/{chr_id}/{LODESTONE_MOUNT_PATH}/", timeout=10)
    if response.status_code == HTTPStatus.FORBIDDEN or response.status_code == HTTPStatus.NOT_FOUND:
        return None
    response.raise_for_status()
    return response.text

def get_achievement_info(chr_id: int) -> str | None:
    response = requests.get(f"{LODESTONE_CHARACTER_BASE_URL}/{chr_id}/{LODESTONE_ACHIEVEMENT_PATH}/", timeout=10)
    if response.status_code == HTTPStatus.FORBIDDEN or response.status_code == HTTPStatus.NOT_FOUND:
        return None    
    response.raise_for_status()
    return response.text