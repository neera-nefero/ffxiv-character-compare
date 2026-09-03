# Process and generates clean character's minions info

from bs4 import BeautifulSoup

from ..constants import NEERA_ID

def process_character_minions(html_response: str) -> list[dict[str, str]]:
    parsed_html = BeautifulSoup(html_response, "html.parser")

    character_minions = extract_minions(parsed_html)
    return character_minions

def extract_minions(parsed_html: BeautifulSoup) -> list[dict[str, str]]:
    content = parsed_html.select_one("div.character__minion")
    if content is None:
        raise ValueError("Character minion content not found in the parser.")

    minions = []

    for minion_element in content.select("li.minion__list_icon[data-tooltip_href]"):
        tooltip_href = minion_element.get("data-tooltip_href")
        if not isinstance(tooltip_href, str):
            raise ValueError("Minion tooltip URL not found in the parser.")

        minions.append({
            "data-tooltip_href": tooltip_href,
        })

    if not minions:
        raise ValueError("No character minions detected in the parser.")
    return minions
