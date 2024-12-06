import pandas as pd
import json

def process_data(raw_data):
    """Convert JSON data to a Pandas DataFrame."""
    data_list = raw_data.get("data", [])
    df = pd.DataFrame(data_list)
    # Convert UNIX timestamps to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    return df

def calculate_statistics(df):
    """Perform basic statistics on the data."""
    stats = {
        "max_value": df["value"].max(),
        "min_value": df["value"].min(),
        "mean_value": df["value"].mean()
    }
    return stats

if __name__ == "__main__":
    with open("../data/raw/fear_greed.json", "r") as file:
        raw_data = json.load(file)
    
    df = process_data(raw_data)
    print(df.head())
    stats = calculate_statistics(df)
    print("Statistics:", stats)
