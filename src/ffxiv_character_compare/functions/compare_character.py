from ..constants import CACHE_FOLDER
from ..character import Character
from ..job import Job
from .utils import file_exists, get_json_file
from .process.process_character_info import generate_chatacter_cache

def compare_character(character_1, character_2):
    obj_char_1: Character = char_json_to_obj(get_char_info(character_1))
    obj_char_2: Character = char_json_to_obj(get_char_info(character_2))
    for compare_line in obj_char_1.compare_characters(obj_char_2):
        print(compare_line)

def get_char_info(character: tuple[int, str]) -> dict:
    char_id = character[0]
    char_name = character[1]
    char_json_file = f"{CACHE_FOLDER}/characters/{char_id}.json"
    if (not file_exists(char_json_file)):
        generate_chatacter_cache(char_name, char_id)
    return get_json_file(char_json_file)

def char_json_to_obj(char_json: dict) -> Character:
    minions_count = len(char_json["minions"])
    mounts_count = len(char_json["mounts"])

    job_list: list[Job] = []
    for job_type in char_json["jobs"]:
        for job in job_type["jobs"]:
            if job["level"] is None:
                job["level"] = 0
            job_list.append(Job(job["name"], job["level"]))

    return Character(char_json["name"], job_list, mounts_count, minions_count, char_json["achievement_points"])



# Process:
# Compare both objects
# Print result