from ..Data import load_data_file


def generate_campaign_regions(name):
    # This will store the full output
    result = {}

    # Define the ranges for each tier
    COLOR_RANGES = {
        "White": range(1, 6),   # 01-05
        "Green": range(6, 11),  # 06-10
        "Blue": range(11, 16),  # 11-15
        "Red": range(16, 21),   # 16-20
        "Black": range(21, 26)  # 21-25
    }

    # Generate the objects for each color
    for color, num_range in COLOR_RANGES.items():
        connects_to = [f"{name} #{num:02}" for num in num_range]
        
        # Create the color object
        result[f"{name} {color}"] = {
            "requires": f"|Progressive Unlock {name}|",
            "connects_to": connects_to
        }
        
        # Create individual objects for each connects_to entry
        for num in num_range:
            result[f"{name} #{num:02}"] = {
                "requires": ""
            }

    return result

# called after the regions.json has been imported, but before ids, etc. have been assigned
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def before_region_table_processed(region_table: dict) -> dict:

    # Get input from input_campaigns.json and create our extra regions
    campaigns = load_data_file("input_campaigns.json")
    
    for campaign in campaigns:
        region_table.update(generate_campaign_regions(campaign))
        region_table["Campaign Select"]["connects_to"].append(f"{campaign} White")
    return region_table
