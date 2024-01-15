import requests
import json

###################################
## FETCH ALL DATA FROM ENDPOINTS ##
###################################

## FETCH AND SAVE ALL DATA FROM ENDPOINTS ##
def fetch_and_save(endpoint, filename):
    url = f"https://esi.evetech.net/dev/universe/{endpoint}/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        with open(f'./gia_app/gia_app/import/data/universe/{filename}.json', 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
        print(f"{filename} data fetched and saved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {filename}: {e}")

## FETCH CATEGORY DETAILS ##
def fetch_category_details(category_id):
    url = f"https://esi.evetech.net/latest/universe/categories/{category_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for category ID: {category_id}")
        return None
    
## FETCH GROUP DETAILS ##
def fetch_group_details(group_id):
    url = f"https://esi.evetech.net/latest/universe/groups/{group_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for group ID: {group_id}")
        return None
    
## FETCH TYPES DETAILS ##
def fetch_types_details(types_id):
    url = f"https://esi.evetech.net/latest/universe/types/{types_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for types ID: {types_id}")
        return None
    
## FETCH GRAPHICS DETAILS ##
def fetch_graphics_details(graphics_id):
    url = f"https://esi.evetech.net/latest/universe/graphics/{graphics_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for graphics ID: {graphics_id}")
        return None

## FETCH CONSTELLATIONS DETAILS ##
def fetch_constellations_details(constellation_id):
    url = f"https://esi.evetech.net/latest/universe/constellations/{constellation_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for contellations ID: {constellation_id}")
        return None

## FETCH REGIONS DETAILS ##
def fetch_regions_details(region_id):
    url = f"https://esi.evetech.net/latest/universe/regions/{region_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for regions ID: {region_id}")
        return None

## FETCH STRUCTURES DETAILS ##
def fetch_structures_details(structure_id):
    url = f"https://esi.evetech.net/latest/universe/structures/{structure_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for structures ID: {structure_id}")
        return None
    
## FETCH SYSTEMS DETAILS ##
def fetch_systems_details(system_id):
    url = f"https://esi.evetech.net/latest/universe/systems/{system_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for systems ID: {system_id}")
        return None



##################################
## SAVE ALL DATA FROM ENDPOINTS ##
##################################    

## SAVE ALL DATA FROM CATEGORIES ##
def fetch_category_data():
    with open('./gia_app/gia_app/import/data/universe/categories.json', 'r') as file:
        category_ids = json.load(file)

    categories_details = []
    for category_id in category_ids:
        details = fetch_category_details(category_id)
        if details:
            categories_details.append(details)

    with open('./gia_app/gia_app/import/data/universe/categories_details.json', 'w') as file:
        json.dump(categories_details, file, indent=4)
    print("Categories details data fetched and saved successfully.")

## SAVE ALL DATA FROM GROUPS ##
def fetch_groups_data():
    with open('./gia_app/gia_app/import/data/universe/groups.json', 'r') as file:
        group_ids = json.load(file)

    groups_details = []
    for group_id in group_ids:
        details = fetch_group_details(group_id)
        if details:
            groups_details.append(details)

    with open('./gia_app/gia_app/import/data/universe/groups_details.json', 'w') as file:
        json.dump(groups_details, file, indent=4)
    print("Groups details data fetched and saved successfully.")

## SAVE ALL DATA FROM GRAPHICS ##
def fetch_graphics_data():
    with open('./gia_app/gia_app/import/data/universe/graphics.json', 'r') as file:
        graphic_ids = json.load(file)

    graphics_details = []
    for graphic_id in graphic_ids:
        details = fetch_graphics_details(graphic_id)
        if details:
            graphics_details.append(details)

    with open('./gia_app/gia_app/import/data/universe/graphics_details.json', 'w') as file:
        json.dump(graphics_details, file, indent=4)
    print("Graphics details data fetched and saved successfully.")

## SAVE ALL DATA FROM CONSTELLATIONS ##
def fetch_constellations_data():
    with open('./gia_app/gia_app/import/data/universe/constellations.json', 'r') as file:
        constellation_ids = json.load(file)

    constellations_details = []
    for constellation_id in constellation_ids:
        details = fetch_constellations_details(constellation_id)
        if details:
            constellations_details.append(details)

    with open('./gia_app/gia_app/import/data/universe/constellations_details.json', 'w') as file:
        json.dump(constellations_details, file, indent=4)
    print("Constellations details data fetched and saved successfully.")

## SAVE ALL DATA FROM REGIONS ##
def fetch_regions_data():
    with open('./gia_app/gia_app/import/data/universe/regions.json', 'r') as file:
        region_ids = json.load(file)

    regions_details = []
    for region_id in region_ids:
        details = fetch_regions_details(region_id)
        if details:
            regions_details.append(details)

    with open('./gia_app/gia_app/import/data/universe/regions_details.json', 'w') as file:
        json.dump(regions_details, file, indent=4)
    print("Regions details data fetched and saved successfully.")

## SAVE ALL DATA FROM STRUCTURES ##
def fetch_structures_data():
    with open('./gia_app/gia_app/import/data/universe/structures.json', 'r') as file:
        structure_ids = json.load(file)

    structures_details = []
    for structure_id in structure_ids:
        details = fetch_structures_details(structure_id)
        if details:
            structures_details.append(details)

    with open('./gia_app/gia_app/import/data/universe/structures_details.json', 'w') as file:
        json.dump(structures_details, file, indent=4)
    print("Structures details data fetched and saved successfully.")

## SAVE ALL DATA FROM SYSTEMS ##
def fetch_systems_data():
    with open('./gia_app/gia_app/import/data/universe/systems.json', 'r') as file:
        system_ids = json.load(file)

    systems_details = []
    for system_id in system_ids:
        details = fetch_systems_details(system_id)
        if details:
            systems_details.append(details)

    with open('./gia_app/gia_app/import/data/universe/systems_details.json', 'w') as file:
        json.dump(systems_details, file, indent=4)
    print("Systems details data fetched and saved successfully.")



##########
## MAIN ##
##########

def main():
    endpoints = {
        'types': 'types',
        'groups': 'groups',
        'ancestries': 'ancestries',
        'bloodlines': 'bloodlines',
        'categories': 'categories',
        'constellations': 'constellations',
        'factions': 'factions',
        'graphics': 'graphics',
        'races': 'races',
        'regions': 'regions',
        'structures': 'structures',
        'systems': 'systems',
        'system_jumps': 'system_jumps',
        'system_kills': 'system_kills',
    }

    for endpoint, filename in endpoints.items():
        fetch_and_save(endpoint, filename)

    # Fetch specific details
    fetch_category_data()
    fetch_groups_data()
    fetch_graphics_data()
    fetch_constellations_data()
    fetch_regions_data()
    fetch_structures_data()
    fetch_systems_data()


if __name__ == "__main__":
    main()
