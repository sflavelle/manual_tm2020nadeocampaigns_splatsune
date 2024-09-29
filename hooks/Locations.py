from ..Data import load_data_file
# called after the locations.json has been imported, but before ids, etc. have been assigned
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py

# Define the ranges for each tier
COLOR_RANGES = {
    "White": range(1, 6),   # 01-05
    "Green": range(6, 11),  # 06-10
    "Blue": range(11, 16),  # 11-15
    "Red": range(16, 21),   # 16-20
    "Black": range(21, 26)  # 21-25
}

MEDALS = ["Bronze", "Silver", "Gold", "Author"]

def generate_campaign_medal_locations(campaign):
    # This will store the full output
    result = []

    # Generate the objects for each color
    for tier, num_range in COLOR_RANGES.items():
        for num in num_range:
            for medal in MEDALS:
                loc = {
                    "name": f"[{campaign}] #{num:02} {medal}",
                    "category": [f"{campaign} {tier}", f"{tier} Medals"],
                    "region": f"{campaign} #{num:02}"
                    }
                result.append(loc)

    return result

def generate_campaign_trophy_locations(campaign):
    # This will store the full output
    result = []

    # Generate the objects for each color
    for tier in COLOR_RANGES.keys():
        for medal in MEDALS:
            loc = {
                "name": f"[{campaign}] {tier} Trophy, All {medal}",
                "category": [f"{campaign} {tier}", f"{campaign} Trophies", f"{tier} Trophies"],
                "region": f"{campaign} {tier}"
                }
            result.append(loc)

    return result

def update_requirements(location_table: list) -> list:
    # Add additional requirements for logic
    pass


def before_location_table_processed(location_table: list) -> list:

    # Get input from input_campaigns.json and create our extra locations
    campaigns = load_data_file("input_campaigns.json")
    
    for campaign in campaigns:
        location_table.extend(generate_campaign_medal_locations(campaign))
        location_table.extend(generate_campaign_trophy_locations(campaign))

    return location_table
