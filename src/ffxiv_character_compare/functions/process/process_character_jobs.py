# Process and generates clean character's job info
# NTH: Extract Eureka, Bozjan, and Occult Crescent

from bs4 import BeautifulSoup

def process_character_jobs(html_response: str) -> list[dict[str, object]]:
    parsed_html = BeautifulSoup(html_response, "html.parser")

    character_jobs = extract_jobs(parsed_html)
    return character_jobs

def extract_jobs(parsed_html: BeautifulSoup) -> list[dict[str, object]]:
    content = parsed_html.select_one("div.character__content")
    if content is None:
        raise ValueError("Character job content not found in the parser.")

    job_types = []

    for heading in content.select("h3.heading--md"):
        type_name = heading.get_text(strip=True)
        if type_name not in ("DoW/DoM", "DoH/DoL"):
            continue

        jobs = []

        for sibling in heading.find_next_siblings():
            if sibling.name == "h3":
                break

            job_elements = sibling.select("ul.character__job > li")

            for job_element in job_elements:
                name_element = job_element.select_one(".character__job__name")
                level_element = job_element.select_one(".character__job__level")

                if name_element is None or level_element is None:
                    continue

                name = name_element.get_text(strip=True)
                level_text = level_element.get_text(strip=True)

                if level_text.isdigit():
                    level = int(level_text)
                else:
                    level = None

                jobs.append({
                    "name": name,
                    "level": level,
                })

        job_types.append({
            "type": type_name,
            "jobs": jobs,
        })

    if not job_types:
        raise ValueError("No character job info detected in the parser.")
    return job_types