
#### **`src/data_processing.py`**

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Loads solar radiation data from a CSV file."""
    return pd.read_csv(file_path, parse_dates=["Timestamp"])

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data: handles missing values and cleans columns."""
    df.fillna(0, inplace=True)
    return df
