import argparse

from .functions.prompt.prompt_character import prompt_character_name
from .functions.prompt.prompt_world import prompt_world_name
from .functions.compare_character import compare_character

def main() -> None:
    parser = argparse.ArgumentParser(
            description="Python tool to compare 2 FFXIV character."
        )
    parser.add_argument(
        "-r",
        "--refresh",
        action="store_true",
        help="Force character and world cache refresh",
    )
    args = parser.parse_args()
    refresh = args.refresh

    character_01 = prompt_character_name(refresh)
    character_02 = prompt_character_name(refresh)
    compare_character(character_01, character_02)