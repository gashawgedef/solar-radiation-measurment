import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


data_folder = '../data'


csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
    print(f"Processing file: {file}")
    
 
    relevant_columns = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'TModA', 'TModB']
    relevant_columns = [col for col in relevant_columns if col in df.columns]
    df = df[relevant_columns].dropna()

 
    for col in relevant_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col], bins=30, kde=True, color='blue', edgecolor='black')
        plt.title(f"Histogram of {col} ({file})")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"Histogram_{col}_{file.split('.')[0]}.png")
        plt.show()

    print(f"Histogram analysis completed for file: {file}")
