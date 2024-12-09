import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def load_and_clean_data(file_path):
    """
    Loads and cleans the dataset.
    - Handles missing values.
    - Replaces negative irradiance values with 0.
    """
    df = pd.read_csv(file_path, parse_dates=["Timestamp"])
    # Fill missing values
    df.fillna(method="ffill", inplace=True)
    df.fillna(method="bfill", inplace=True)

    # Replace negative values in irradiance columns
    irradiance_cols = ["GHI", "DNI", "DHI", "ModA", "ModB"]
    df[irradiance_cols] = df[irradiance_cols].clip(lower=0)

    return df


def summary_statistics(df):
    """Prints summary statistics for numeric columns."""
    print("\nSummary Statistics:\n")
    print(df.describe())


def data_quality_check(df):
    """Checks for missing values, outliers, and negative values."""
    print("\nData Quality Check:")
    print("Missing Values:\n", df.isnull().sum())

    # Outlier detection using Z-scores
    z_scores = np.abs((df.select_dtypes(include=[np.number]) - df.mean()) / df.std())
    outliers = (z_scores > 3).sum()
    print("\nOutliers Detected:\n", outliers)


def time_series_analysis(df):
    """Plots time series analysis for GHI, DNI, DHI, and Tamb."""
    plt.figure(figsize=(12, 6))
    for col, color in zip(["GHI", "DNI", "DHI"], ["orange", "blue", "green"]):
        plt.plot(df["Timestamp"], df[col], label=col, color=color)
    plt.xlabel("Timestamp")
    plt.ylabel("Irradiance (W/m²)")
    plt.title("Solar Irradiance Over Time")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("solar_time_series.png")
    print("\nTime series plot saved as 'solar_time_series.png'.")


def cleaning_impact_analysis(df):
    """Evaluates the impact of cleaning on sensor readings."""
    plt.figure(figsize=(10, 5))
    sns.boxplot(x="Cleaning", y="ModA", data=df)
    plt.title("Impact of Cleaning on ModA Readings")
    plt.savefig("cleaning_modA_impact.png")
    print("\nCleaning impact plot saved as 'cleaning_modA_impact.png'.")


def correlation_analysis(df):
    """Generates correlation matrix heatmap."""
    plt.figure(figsize=(12, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig("correlation_matrix.png")
    print("\nCorrelation matrix heatmap saved as 'correlation_matrix.png'.")


def wind_analysis(df):
    """Generates wind rose plot for wind direction and speed."""
    fig = px.scatter_polar(
        df, r="WS", theta="WD", color="WS", title="Wind Rose (Speed vs Direction)"
    )
    fig.write_html("wind_rose.html")
    print("\nWind rose plot saved as 'wind_rose.html'.")


def temperature_analysis(df):
    """Examines the relationship between RH and Tamb."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x="RH",
        y="Tamb",
        hue="GHI",
        size="DNI",
        data=df,
        palette="coolwarm",
        sizes=(20, 200),
    )
    plt.title("Temperature vs Humidity vs Solar Irradiance")
    plt.xlabel("Relative Humidity (%)")
    plt.ylabel("Ambient Temperature (°C)")
    plt.savefig("temp_humidity_impact.png")
    print(
        "\nTemperature-humidity relationship plot saved as 'temp_humidity_impact.png'."
    )


def histograms(df):
    """Creates histograms for GHI, DNI, DHI, WS, and Tamb."""
    plt.figure(figsize=(12, 6))
    columns = ["GHI", "DNI", "DHI", "WS", "Tamb"]
    for i, col in enumerate(columns, 1):
        plt.subplot(2, 3, i)
        plt.hist(df[col], bins=20, color="skyblue", edgecolor="black")
        plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig("histograms.png")
    print("\nHistograms saved as 'histograms.png'.")


def z_score_analysis(df):
    """Flags significant outliers using Z-scores."""
    z_scores = np.abs((df.select_dtypes(include=[np.number]) - df.mean()) / df.std())
    outliers = z_scores > 3
    flagged_data = df[outliers.any(axis=1)]
    print(f"\nSignificant Outliers Found:\n{flagged_data}")


def bubble_chart(df):
    """Generates a bubble chart to explore complex relationships."""
    fig = px.scatter(
        df,
        x="GHI",
        y="Tamb",
        size="RH",
        color="WS",
        title="Bubble Chart: GHI vs Tamb vs RH (size) & WS (color)",
        labels={
            "GHI": "Global Horizontal Irradiance (W/m²)",
            "Tamb": "Ambient Temperature (°C)",
            "RH": "Relative Humidity (%)",
            "WS": "Wind Speed (m/s)",
        },
    )
    fig.write_html("bubble_chart.html")
    print("\nBubble chart saved as 'bubble_chart.html'.")


def main():
    # Replace 'solar_radiation_data.csv' with your dataset path
    file_path = "solar_radiation_data.csv"
    df = load_and_clean_data(file_path)

    summary_statistics(df)
    data_quality_check(df)
    time_series_analysis(df)
    cleaning_impact_analysis(df)
    correlation_analysis(df)
    wind_analysis(df)
    temperature_analysis(df)
    histograms(df)
    z_score_analysis(df)
    bubble_chart(df)


if __name__ == "__main__":
    main()
