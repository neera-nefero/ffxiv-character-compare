from .prompt_filter import prompt_filter
from ..get_online.get_online_character import search_character

def prompt_character() -> str:
    while (True):
        filter = None
        filter_prefix = None
        if (prompt_input_option() == 2):
            filter, filter_prefix = prompt_filter()
            
        chr_name = prompt_chr_name()
        search_result = search_character(chr_name, filter, filter_prefix)
        if search_result["total"] == 0:
            print(f"No players found with your criteria")
            continue
        print(f"chr_id: -- {prompt_chr_list(search_result)}")


     
        
    return "None"

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

def prompt_chr_name() -> str:
    while True:
        response = input("Input the name of the character: ").strip()
        if response != "":
            return response
        print(f"Please insert some value")

def prompt_chr_list(search_result) -> int:
    list_total = len(search_result["results"])
    if (list_total < search_result["total"]):
        print(f"Showing {list_total} from total result of {search_result["total"]}")

    for i in range(0, list_total):
        chr_name = search_result["results"][i]["name"]
        chr_world = search_result["results"][i]["world"]
        print(f"{i} - {chr_name} from {chr_world}")
    print(f"{i + 1} - Search character again")

    while True:
        response = input("Selection: ").strip()
        try:
            selected_index = int(response)
        except ValueError:
            print("Please enter a number")
            continue
        if selected_index >= 0 and selected_index < list_total:
            return search_result["results"][selected_index]["chr_id"]
        if selected_index == list_total:
            return -1
        print(f"Please insert a valid value")    
    
    return True