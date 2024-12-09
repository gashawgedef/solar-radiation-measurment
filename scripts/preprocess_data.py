import pandas as pd


def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    # Handle missing values
    df.fillna(method="ffill", inplace=True)
    return df
