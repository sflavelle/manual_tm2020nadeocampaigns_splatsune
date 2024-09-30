# Here is the data we need for everything

CAMPAIGN_TIERS = {
    "White": range(1, 6),   # 01-05
    "Green": range(6, 11),  # 06-10
    "Blue": range(11, 16),  # 11-15
    "Red": range(16, 21),   # 16-20
    "Black": range(21, 26)  # 21-25
}

MEDALS = ["Bronze", "Silver", "Gold", "Author"]
TIER_ORDER = ["White", "Green", "Blue", "Red", "Black"]

CAMPAIGNS = [
    "Training",
    "Custom",
    "Summer 2020",
    "Fall 2020",
    "Winter 2021",
    "Spring 2021",
    "Summer 2021",
    "Fall 2021",
    "Winter 2022",
    "Spring 2022",
    "Summer 2022",
    "Fall 2022",
    "Winter 2023",
    "Spring 2023",
    "Summer 2023",
    "Fall 2023",
    "Winter 2024",
    "Spring 2024",
    "Summer 2024",
    "Fall 2024"
]

def supported_campaigns() -> list:
    return CAMPAIGNS

# Processing functions for regions and locations
def generate_campaign_regions(campaign):
    result = {}

    for i, tier in enumerate(TIER_ORDER):
        num_range = CAMPAIGN_TIERS[tier]
        connects_to = [f"{campaign} #{num:02}" for num in num_range]
        
        # Create the tier region
        result[f"{campaign} {tier}"] = {
            "requires": f"|Progressive Unlock {campaign}:{i+1}|",
            "connects_to": connects_to
        }

        # Connect each region to the next tier
        if i < len(TIER_ORDER) - 1:
            next_tier = TIER_ORDER[i + 1]
            result[f"{campaign} {tier}"]["connects_to"].append(f"{campaign} {next_tier}")

        for num in num_range:
            result[f"{campaign} #{num:02}"] = {
                "requires": ""
            }

    return result

def generate_campaign_medal_locations(campaign):
    # This will store the full output
    result = []

    # Generate the objects for each color
    for tier, num_range in CAMPAIGN_TIERS.items():
        for num in num_range:
            for medal in MEDALS:
                loc = {
                    "name": f"[{campaign}] #{num:02} {medal}",
                    "category": [f"{campaign} {tier}", f"Medals - {medal}"],
                    "region": f"{campaign} #{num:02}"
                    }
                if num == 25 and medal == "Gold":
                    loc["place_item"] = ["Campaign Completion Token"]
                result.append(loc)

    return result

def generate_campaign_trophy_locations(campaign):
    # This will store the full output
    result = []

    # Generate the objects for each color
    for tier in CAMPAIGN_TIERS.keys():
        for medal in MEDALS:
            loc = {
                "name": f"[{campaign}] Trophy - {tier}, All {medal}",
                "category": [f"{campaign} {tier}", f"{campaign} Trophies", "Trophies"],
                "region": f"{campaign} {tier}"
                }
            result.append(loc)

    return result

def generate_campaign_unlock_items(campaign):
    result = []
    progressive_item = {
        "name": f"Progressive Unlock {campaign}",
        "category": ["Campaign Unlocks"],
        "progression": True,
        "count": 5
        }
    result.append(progressive_item)
    return result

# ############
# And now the actual hooks
# ############

# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table
# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    for campaign in CAMPAIGNS:
        item_table.extend(generate_campaign_unlock_items(campaign))
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:

    for campaign in CAMPAIGNS:
        location_table.extend(generate_campaign_medal_locations(campaign))
        location_table.extend(generate_campaign_trophy_locations(campaign))

    return location_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:

    for campaign in CAMPAIGNS:
        region_table.update(generate_campaign_regions(campaign))
        region_table["Campaign Select"]["connects_to"].append(f"{campaign} White")
    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    return category_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table

# called when an external tool (eg Univeral Tracker) ask for slot data to be read
# use this if you want to restore more data
# return True if you want to trigger a regeneration if you changed anything
def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> bool:
    return False
