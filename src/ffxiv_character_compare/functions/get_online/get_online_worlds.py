# Gets online info from the datacenters and worlds

import requests

from ..process.process_worlds_info import process_worlds
from ...constants import LODESTONE_WORLD_BASE_URL

def get_worlds_info() -> None:
    response = requests.get(LODESTONE_WORLD_BASE_URL, timeout=10)
    response.raise_for_status()
    
    process_worlds(response.text)
    return None