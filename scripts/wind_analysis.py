import pandas as pd
import os
import matplotlib.pyplot as plt
from windrose import WindroseAxes
import numpy as np


data_folder = '../data'


csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
    print(f"Processing file: {file}")
    
 
    wind_columns = ['WS', 'WSgust', 'WD', 'WDstdev']
    wind_columns = [col for col in wind_columns if col in df.columns]
    
    if 'WD' not in wind_columns or 'WS' not in wind_columns:
        print(f"Wind data not found in {file}. Skipping.")
        continue
    

    df = df.dropna(subset=wind_columns)
    df = df[df['WS'] >= 0] 


    plt.figure(figsize=(8, 8))
    ax = WindroseAxes.from_ax()
    ax.bar(df['WD'], df['WS'], normed=True, opening=0.8, edgecolor='black', cmap='coolwarm')
    ax.set_title(f"Wind Rose for {file}")
    ax.set_legend()
    plt.savefig(f"wind_rose_{file.split('.')[0]}.png")
    plt.show()

   
    bins = np.arange(0, 360, 30)
    df['WD_bin'] = pd.cut(df['WD'], bins=bins, labels=bins[:-1], right=False)
    
 
    wind_data = df.groupby('WD_bin')['WS'].mean().reset_index()
    wind_data['WD_bin'] = wind_data['WD_bin'].astype(int)

    theta = np.deg2rad(wind_data['WD_bin'])
    radii = wind_data['WS']
    width = np.deg2rad(30)

    ax = plt.subplot(111, polar=True)
    bars = ax.bar(theta, radii, width=width, bottom=0, color='blue', edgecolor='black', alpha=0.7)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    plt.title(f"Radial Bar Plot for {file}")
    plt.savefig(f"radial_bar_plot_{file.split('.')[0]}.png")
    plt.show()

    print(f"Wind analysis completed for file: {file}")
