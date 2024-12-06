import requests
import json
from config import API_KEY

# API endpoint
BASE_URL = "https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical"

def fetch_fear_and_greed_data(start=None, limit=50):
    """Fetch historical Fear and Greed Index data from the CoinMarketCap API."""
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY
    }
    params = {
        "start": start,
        "limit": limit
    }
    
    response = requests.get(BASE_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

def save_data_to_file(data, filename):
    """Save fetched data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    try:
        data = fetch_fear_and_greed_data(limit=100)
        save_data_to_file(data, "../data/raw/fear_greed.json")
    except Exception as e:
        print(e)
