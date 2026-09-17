# Request online info from the selected character

import requests
from http import HTTPStatus

from ..process.process_character_search import process_search
from ...constants import LODESTONE_CHARACTER_BASE_URL, LODESTONE_JOB_PATH, LODESTONE_MINION_PATH, LODESTONE_MOUNT_PATH, LODESTONE_ACHIEVEMENT_PATH

def search_character(chr_name: str, world: str | None = None, world_prefix: str | None = None) -> dict[str, object]:
    query_name = chr_name.replace(" ", "+")
    worldname = f"{world_prefix or ''}{world or ''}"

    request_url = f"{LODESTONE_CHARACTER_BASE_URL}/?q={query_name}&worldname={worldname}"
    response = requests.get(request_url, timeout=10)
    response.raise_for_status()

    search_result = process_search(response.text)
    return search_result

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