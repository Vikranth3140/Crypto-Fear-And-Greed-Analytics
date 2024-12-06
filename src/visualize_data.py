import pandas as pd
import matplotlib.pyplot as plt

def plot_fear_and_greed(df):
    """Plot the Fear and Greed Index over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(df["timestamp"], df["value"], label="Fear and Greed Index", marker="o")
    plt.xlabel("Date")
    plt.ylabel("Index Value")
    plt.title("Fear and Greed Index Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/fear_greed.csv")
    plot_fear_and_greed(df)
