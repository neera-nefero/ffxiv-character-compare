import shutil
import json
from pathlib import Path


def delete_folder(folder: str) -> None:
    shutil.rmtree(folder, ignore_errors=True)
    return None

def file_exists(file: str) -> bool:
    return Path(file).is_file()

def get_json_file(file: str) -> dict:
    data = json.load(Path(file).open("r", encoding="utf-8"))
    return data