import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create figure
    fig, ax = plt.subplots()

    # Scatter plot
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First regression (1880–2050)
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years_extended = pd.Series(range(1880, 2051))
    ax.plot(
        years_extended,
        result.intercept + result.slope * years_extended,
        'r'
    )

    # Second regression (2000–2050)
    df_recent = df[df["Year"] >= 2000]

    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent_extended = pd.Series(range(2000, 2051))
    ax.plot(
        years_recent_extended,
        result_recent.intercept + result_recent.slope * years_recent_extended,
        'g'
    )

    # Labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    return fig   # ✅ IMPORTANT