import pandas as pd
import os

data_folder = '../data'

csv_files =[ file for file in os.listdir(data_folder) if file.endswith('.csv')]

positive_value_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
    print("========================================")
    print(f"Processing file: {file}")

 
    missing_values = df.isnull().sum()
    missing_percent = (missing_values / len(df)) * 100
    print("\nMissing Values Summary:")
    print(pd.DataFrame({'Missing Values': missing_values, 'Percentage (%)': missing_percent}).query("`Missing Values` > 0"))


    print("\nNegative Values Check:")
    for col in positive_value_columns:
        if col in df.columns:
            negative_count = (df[col] < 0).sum()
            if negative_count > 0:
                print(f"Column '{col}' has {negative_count} negative values.")


    print("\nOutliers Check:")
    outlier_columns = ['ModA', 'ModB', 'WS', 'WSgust']
    for col in outlier_columns:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            print(f"Column '{col}' has {len(outliers)} outliers.")

    print("=====================================================")


