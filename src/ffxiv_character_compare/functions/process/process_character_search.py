from bs4 import BeautifulSoup
from ..get_online.get_online_character import search_character

TOTAL_FILTER = "div.parts__total"
ERROR_MESSAGE_FILTER = "p.form__message--error"
ENTRY_FILTER = "div.entry:not(.more_)"
ENTRY_NAME_FILTER = "p.entry__name"
ENTRY_WORLD_FILTER = "p.entry__world"

def process_search(html_response: str) -> dict[str, object]:
    parsed_html = BeautifulSoup(html_response, "html.parser")

    search_result = extract_search_result(parsed_html)
    return search_result

def extract_search_result(parsed_html: BeautifulSoup) -> dict[str, object]:
    search_result: dict[str, object] = {}

    total_html = parsed_html.select_one(TOTAL_FILTER)
    if total_html is not None:
        total_text = total_html.get_text(strip=True)
        search_result["total"] = int(total_text.split()[0])

    error_message_html = parsed_html.select_one(ERROR_MESSAGE_FILTER)
    if error_message_html is not None:
        search_result["error"] = {"message": error_message_html.get_text(strip=True)}

    results = []
    for entry in parsed_html.select(ENTRY_FILTER):
        name_html = entry.select_one(ENTRY_NAME_FILTER)
        world_html = entry.select_one(ENTRY_WORLD_FILTER)
        if name_html is None or world_html is None:
            raise ValueError("Character entry is missing name or world in the parser.")

        results.append(
            {
                "name": name_html.get_text(strip=True),
                "world": world_html.get_text(strip=True),
            }
        )
    search_result["results"] = results

    return search_result

if __name__ == "__main__":
    pass