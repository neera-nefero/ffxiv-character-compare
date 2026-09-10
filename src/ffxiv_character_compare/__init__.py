import argparse

from .functions.prompt.prompt_character import prompt_character
from .functions.compare_character import compare_character

def main() -> None:
    try:
        parser = argparse.ArgumentParser(
                description="Python tool to compare 2 FFXIV character."
            )
        parser.add_argument(
            "-r",
            "--refresh",
            action="store_true",
            help="Force character and world cache refresh",
        )
        # NTH - Some ASCII Art
        print(f"Welcome to FFXIV Compare")

        args = parser.parse_args()
        refresh = args.refresh

        print(f"Selecting character 1")
        character_01 = prompt_character(refresh)

        print(f"Selecting character 2")
        character_02 = prompt_character(refresh)
        compare_character(character_01, character_02)

    except KeyboardInterrupt:
        print("\nFFXIV Compare cancelled by user.")
        raise SystemExit(130) from None


