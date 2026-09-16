from ..get_online.get_online_worlds import get_worlds_info
from ..utils import file_exists, get_json_file
from ...constants import CACHE_FOLDER, LODESTONE_WORLD_FILTER_PREFIX, LODESTONE_LOGICAL_DC_FILTER_PREFIX, LODESTONE_PHYSICAL_DC_FILTER_PREFIX

def prompt_filter() -> tuple[str, str] :
    worlds_json_file = f"{CACHE_FOLDER}/worlds.json"
    if (not file_exists(worlds_json_file)):
        get_worlds_info()
    dc_dict = get_json_file(worlds_json_file)
    regions = dc_dict["regions"]

    # NTH - Check dc_dict["updated_at"] and if too old regenerate 

    # Region selection - mandatory
    region_list: list[str] = []
    for region in regions:
        region_list.append(region["name"])
    print("Select the region:")
    region_selection = prompt_filter_options(region_list, False)

    # DC selection - optional
    dc_list: list[str] = []
    for dc in regions[region_selection]["logical_dcs"]:
        dc_list.append(dc["name"])
    print("(Optional) Select the data center:")
    dc_selection = prompt_filter_options(dc_list, True)

    # World selection - optional
    world_list: list[str] = []
    if dc_selection == -1:
        for dc in regions[region_selection]["logical_dcs"]:
            for world in dc["worlds"]:
                world_list.append(world["name"])
    else:
        for world in regions[region_selection]["logical_dcs"][dc_selection]["worlds"]:
            world_list.append(world["name"])
    print("(Optional) Select the world:")
    world_selection = prompt_filter_options(world_list, True)

    if world_selection != -1:
        return (world_list[world_selection], LODESTONE_WORLD_FILTER_PREFIX)
    if dc_selection != -1:
        return (dc_list[dc_selection], LODESTONE_LOGICAL_DC_FILTER_PREFIX)
    return (regions[region_selection]["id"], LODESTONE_LOGICAL_DC_FILTER_PREFIX)

def prompt_filter_options(option_list: list[str], optional: bool = False) -> int:
    for i in range(0, len(option_list)):
        print(f"{i} - {option_list[i]}")

    while True:
        response = input("Selection: ").strip()
        if optional and response == "":
            return -1       
        try:
            selected_index = int(response)
        except ValueError:
            print("Please enter a number")
            continue        
        if selected_index >= 0 and selected_index < len(option_list):
            return selected_index
        print(f"Please insert a valid value")