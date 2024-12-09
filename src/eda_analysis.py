import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def summarize_statistics(df):
    return df.describe()


def plot_time_series(df, columns, title="Time Series Analysis"):
    df.set_index("Timestamp")[columns].plot(figsize=(10, 5))
    plt.title(title)
    plt.show()


def plot_correlation_matrix(df):
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()
