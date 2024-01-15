import requests
import json

def fetch_group_details(group_id):
    url = f"https://esi.evetech.net/latest/universe/groups/{group_id}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            group_data = response.json()
            type_ids = group_data.get("types", [])  # Assuming 'types' is the key for type IDs
            return type_ids
        else:
            print(f"Failed to fetch data for group ID: {group_id}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for group ID: {group_id}: {e}")
        return None


def fetch_type_details(type_id):
    # Fetch detailed information for the type
    pass

def fetch_material_breakdown(type_id):
    # Recursively fetch raw material breakdown for the type
    pass

def main():
    with open('./data/universe/categories_details.json', 'r') as file:
        categories_details = json.load(file)
    
    blueprints = {}
    for group_id in categories_details['groups']:
        type_ids = fetch_group_details(group_id)
        for type_id in type_ids:
            type_details = fetch_type_details(type_id)
            blueprints[type_id] = {
                'details': type_details,
                'materials': fetch_material_breakdown(type_id)
            }

    with open('blueprints.json', 'w') as file:
        json.dump(blueprints, file, indent=4)

if __name__ == "__main__":
    main()
