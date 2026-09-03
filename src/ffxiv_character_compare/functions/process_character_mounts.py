# Process and generates clean character's mounts info

from bs4 import BeautifulSoup

def process_character_mounts(html_response: str) -> list[dict[str, str]]:
    parsed_html = BeautifulSoup(html_response, "html.parser")

    character_mounts = extract_mounts(parsed_html)
    return character_mounts

def extract_mounts(parsed_html: BeautifulSoup) -> list[dict[str, str]]:
    content = parsed_html.select_one("div.character__mounts")
    if content is None:
        raise ValueError("Character mount content not found in the parser.")

    mounts = []

    for mount_element in content.select("li.mount__list_icon[data-tooltip_href]"):
        tooltip_href = mount_element.get("data-tooltip_href")
        if not isinstance(tooltip_href, str):
            raise ValueError("Mount tooltip URL not found in the parser.")

        mounts.append({
            "data-tooltip_href": tooltip_href,
        })

    if not mounts:
        raise ValueError("No character mounts detected in the parser.")
    return mounts
