import shutil
from pathlib import Path

def delete_folder(folder: str) -> None:
    shutil.rmtree(folder, ignore_errors=True)
    return None

def file_exists(file: str) -> bool:
    return Path(file).is_file()