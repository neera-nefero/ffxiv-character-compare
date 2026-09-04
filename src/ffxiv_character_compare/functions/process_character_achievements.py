# Process and generates clean character achievement points

from bs4 import BeautifulSoup

from .get_online_character import get_achievement_info
from ..constants import NEERA_ID


def process_character_achievements(html_response: str | None) -> int:
    if html_response is None:
        return 0
    
    parsed_html = BeautifulSoup(html_response, "html.parser")

    achievement_points = extract_achievement_points(parsed_html)
    return achievement_points


def extract_achievement_points(parsed_html: BeautifulSoup) -> int:
    points_element = parsed_html.select_one("p.achievement__point")
    if points_element is None:
        raise ValueError("Character achievement points not found in the parser.")

    points_text = points_element.get_text(strip=True).replace(",", "")
    if not points_text.isdigit():
        raise ValueError("Character achievement points are not a valid number.")

    return int(points_text)