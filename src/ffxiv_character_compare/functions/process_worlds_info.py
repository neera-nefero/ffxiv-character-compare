# Process and generates clean datacenters and worlds info

from bs4 import BeautifulSoup

from .get_online_worlds import get_worlds_info

PHYSICAL_DC_FILTER = "ul.world__tab li[data-region]"

def process_worlds(html_response: str) -> None:
    parsed_html = BeautifulSoup(html_response, "html.parser")
    
    region_items = extract_physicals_dc(parsed_html)

def extract_physicals_dc(parsed_html) -> list[dict[str, str]]:
    region_items = parsed_html.select(PHYSICAL_DC_FILTER)
    regions = []

    for item in region_items:
        region = {
            "id": int(item["data-region"]),
            "name": item.find("span").get_text(strip=True),
        }
        regions.append(region)

    if len(regions) == 0:
        raise Exception("Not physical DC detected in the parser.")
    return regions

if __name__ == "__main__":
    html_response = get_worlds_info()
    process_worlds(html_response)
