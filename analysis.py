import requests

# Your API key
API_KEY = "your_api_key_here"

# API endpoint
url = "https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical"

# Headers with API Key
headers = {
    "X-CMC_PRO_API_KEY": API_KEY
}

# Query parameters (if applicable, e.g., date range)
params = {
    "time_start": "2023-01-01",
    "time_end": "2023-12-31",
    "limit": 100
}

# Making the GET request
response = requests.get(url, headers=headers, params=params)

# Parsing JSON data
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}, {response.text}")
