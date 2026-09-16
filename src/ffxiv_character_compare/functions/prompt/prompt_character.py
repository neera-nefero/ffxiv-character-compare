from .prompt_filter import prompt_filter
from ..get_online.get_online_character import search_character

def prompt_character() -> str | None:
    match(prompt_input_option()):
        case 1:
            character_name = prompt_character_name()            
            return search_character(character_name)
        case 2:
            character_name = prompt_character_name() 
            filter, filter_prefix = prompt_filter()
            return search_character(character_name, filter, filter_prefix)

def prompt_input_option() -> int:
    print(f"Do you know the exact name of the character?")
    print(f"1. Yes")
    print(f"2. No")

    while True:
        response = input("Selection: ").strip()

        try:
            selected_index = int(response)
        except ValueError:
            print("Please enter a number.")
            continue

        if selected_index == 1 or selected_index == 2:
            return selected_index
        print(f"Please input 1 or 2")

def prompt_character_name() -> str:
    while True:
        response = input("Input the name of the character: ").strip()
        if response != "":
            return response
        print(f"Please insert some value")