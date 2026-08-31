# Gets online info from the datacenters and worlds

import requests

from ..constants import LODESTONE_WORLD_BASE_URL

def get_worlds_info() -> str:
    response = requests.get(LODESTONE_WORLD_BASE_URL, timeout=10)
    response.raise_for_status()

    return response.text