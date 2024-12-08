import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data_folder = '../data'


csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]


def calculate_z_scores(df, relevant_columns):
    z_scores = (df[relevant_columns] - df[relevant_columns].mean()) / df[relevant_columns].std()
    outliers = (z_scores.abs() > 3)  
    return z_scores, outliers

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
    print(f"Processing file: {file}")
    
    
    relevant_columns = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'TModA', 'TModB']
    relevant_columns = [col for col in relevant_columns if col in df.columns]
    df = df[relevant_columns].dropna()
    
   
    z_scores, outliers = calculate_z_scores(df, relevant_columns)
    

    print(f"Z-Scores for file: {file}")
    print(z_scores.head()) 
    
    print(f"\nOutliers (Z-score > 3 or < -3):")
    print(outliers.head())  
    
   
    outliers_filename = f"outliers_{file.split('.')[0]}.csv"
    outliers.to_csv(outliers_filename, index=False)
    
   
    for col in relevant_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col], bins=30, kde=True, color='blue', edgecolor='black', label='Data')
        
       
        plt.scatter(df.index[outliers[col]], df[col][outliers[col]], color='red', label='Outliers', zorder=5)
        
        plt.title(f"Z-Score Analysis for {col} ({file})")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"Z_Score_Analysis_{col}_{file.split('.')[0]}.png")
        plt.show()
    
    print(f"Z-Score analysis completed for file: {file}")
