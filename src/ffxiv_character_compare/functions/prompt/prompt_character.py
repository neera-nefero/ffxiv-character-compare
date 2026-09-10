from ..get_online.get_online_character import search_character

def prompt_character(refresh) -> str | None:
    match(prompt_input_option()):
        case 1:
            character_name = prompt_character_name()            
            return search_character(character_name)
        case 2:
            character_name = prompt_character_name() 
            world, world_prefix = prompt_world(refresh)
            return search_character(character_name, world, world_prefix)

def prompt_input_option() -> int:
    print(f"Do you know the exact the name of the character?")
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

def prompt_world(refresh: bool) -> tuple[str, str] :
    # First need to check the cache data or refresh if asked
    # #

    # Go to phys, then logic finally world. Return the most right selection


    return ("world", "world_prefix")