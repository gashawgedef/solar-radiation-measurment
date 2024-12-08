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
 
    relevant_columns = ['RH', 'Tamb', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']
    relevant_columns = [col for col in relevant_columns if col in df.columns]
    df = df[relevant_columns].dropna()

 
    plt.figure(figsize=(10, 6))
    for temp_col in ['Tamb', 'TModA', 'TModB']:
        if temp_col in df.columns:
            sns.scatterplot(x=df['RH'], y=df[temp_col], label=temp_col)
    plt.title(f"Relative Humidity vs Temperature ({file})")
    plt.xlabel("Relative Humidity (%)")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"RH_vs_Temperature_{file.split('.')[0]}.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    for rad_col in ['GHI', 'DNI', 'DHI']:
        if rad_col in df.columns:
            sns.scatterplot(x=df['RH'], y=df[rad_col], label=rad_col)
    plt.title(f"Relative Humidity vs Solar Radiation ({file})")
    plt.xlabel("Relative Humidity (%)")
    plt.ylabel("Solar Radiation (W/m²)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"RH_vs_SolarRadiation_{file.split('.')[0]}.png")
    plt.show()

  
    print("\nCorrelation Analysis:")
    correlation_matrix = df.corr()
    print(correlation_matrix[['RH']]) 
    
   
    correlation_matrix.to_csv(f"correlation_analysis_{file.split('.')[0]}.csv", index=True)

    print(f"Temperature analysis completed for file: {file}")
