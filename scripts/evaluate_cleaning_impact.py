import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


data_folder = '../data'


csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]


for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])

    print(f"Processing file: {file}")


    if 'Cleaning' not in df.columns:
        print(f"Skipping file {file} as it lacks a 'Cleaning' column.")
        continue

 
    cleaned = df[df['Cleaning'] == 1]
    not_cleaned = df[df['Cleaning'] == 0]

  
    for col in ['ModA', 'ModB']:
        if col in df.columns:
            print(f"\nSensor: {col}")
            print(f"Average reading when cleaned: {cleaned[col].mean():.2f}")
            print(f"Average reading when not cleaned: {not_cleaned[col].mean():.2f}")
            print(f"Difference: {cleaned[col].mean() - not_cleaned[col].mean():.2f}")

    for col in ['ModA', 'ModB']:
        if col in df.columns:
            plt.figure(figsize=(12, 6))
            sns.boxplot(data=df, x='Cleaning', y=col, palette='Set2')
            plt.title(f"Impact of Cleaning on {col} ({file})")
            plt.xlabel("Cleaning (0 = Not Cleaned, 1 = Cleaned)")
            plt.ylabel(col)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.savefig(f"cleaning_impact_{col}_{file.split('.')[0]}.png")
            plt.show()

    print(f"Plots saved for file: {file}")
