import pandas as pd
import matplotlib.pyplot as plt

def plot_fear_and_greed(csv_file):
    """Plot the Fear and Greed Index over time."""
    df = pd.read_csv(csv_file)
    df["timestamp"] = pd.to_datetime(df["timestamp"])\

    plt.figure(figsize=(10, 6))
    plt.plot(df["timestamp"], df["value"], label="Fear and Greed Index", marker="o")

    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))

    plt.xlabel("Date")
    plt.ylabel("Index Value")
    plt.title("Fear and Greed Index Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fear_and_greed("../data/processed/fear_greed.csv")
