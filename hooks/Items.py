from ..Data import load_data_file

# called after the items.json has been imported, but before ids, etc. have been assigned
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def before_item_table_processed(item_table: list) -> list:

    # Get input from input_campaigns.json and create our extra locations
    campaigns = load_data_file("input_campaigns.json")
    
    for campaign in campaigns:
        item_table.append({
                    "name": f"Progressive Unlock {campaign}",
                    "category": ["Campaign Unlocks"],
                    "progression": True,
                    "count": 5
                    })

    return item_table
