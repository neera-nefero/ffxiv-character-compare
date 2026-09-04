# Process and generates clean datacenters and worlds info

import json
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

from ..get_online.get_online_worlds import get_worlds_info

PHY_DC_FILTER = "ul.world__tab li[data-region]"
REGION_FILTER = "div.js--tab-content[data-region]"
LOG_DC_FILTER = "li.world-dcgroup__item"
LOG_DC_NAME_FILTER = "h2.world-dcgroup__header"
WORLD_NAME_FILTER = ".world-list__world_name p"

def process_worlds(html_response: str) -> None:
    parsed_html = BeautifulSoup(html_response, "html.parser")

    regions = extract_worlds(parsed_html)
    generate_worlds_cache(regions)

def extract_worlds(parsed_html: BeautifulSoup) -> list[dict[str, object]]:
    physical_names: dict[int, str] = {}
    regions: list[dict[str, object]] = []

    region_items = parsed_html.select(PHY_DC_FILTER)

    for item in region_items:
        region_id_value = item.get("data-region")
        if not isinstance(region_id_value, str):
            raise ValueError("Physical data center region ID not found in the parser.")

        region_id = int(region_id_value)
        region_name = item.get_text(strip=True)

        physical_names[region_id] = region_name

    if not physical_names:
        raise ValueError("No physical data centers detected in the parser.")

    for region_html in parsed_html.select(REGION_FILTER):
        region_id_value = region_html.get("data-region")
        if not isinstance(region_id_value, str):
            raise ValueError("Data center region ID not found in the parser.")

        region_id = int(region_id_value)
        logical_dcs = []

        for logical_html in region_html.select(LOG_DC_FILTER):
            heading = logical_html.select_one(LOG_DC_NAME_FILTER)
            if heading is None:
                raise ValueError("Logical data center name not found in the parser.")

            worlds = [
                {"name": world.get_text(strip=True)}
                for world in logical_html.select(WORLD_NAME_FILTER)
            ]
            logical_dcs.append(
                {
                    "name": heading.get_text(strip=True),
                    "worlds": worlds,
                }
            )

        region = {
            "id": region_id,
            "name": physical_names[region_id],
            "logical_dcs": logical_dcs,
        }
        regions.append(region)

    if not regions:
        raise ValueError("No data centers detected in the parser.")
    return regions


def generate_worlds_cache(regions: list[dict[str, object]]) -> None:
    cache_path = Path("data/cache/worlds.json")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    json_content = {
        "updated_at": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        "regions": regions,
    }

    with cache_path.open("w", encoding="utf-8") as file:
        json.dump(json_content, file, indent=2, ensure_ascii=False)
