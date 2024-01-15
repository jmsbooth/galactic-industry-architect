import requests
import json

def fetch_and_save(endpoint, filename):
    url = f"https://esi.evetech.net/latest/markets/{endpoint}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        with open(f'./data/market/{filename}.json', 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
        print(f"{filename} data fetched and saved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {filename}: {e}")

def main():
    market_endpoints = {
        'groups': 'groups',
        'prices': 'prices',
        # Example: 'market_orders': 'orders', 'market_prices': 'prices'
        # Add additional market endpoints here
    }

    for endpoint, filename in market_endpoints.items():
        fetch_and_save(endpoint, filename)

if __name__ == "__main__":
    main()
