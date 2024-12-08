import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

data_folder = '../data'

csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]

columns_to_plot = ['GHI', 'DNI', 'DHI', 'Tamb']

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    print(f"Processing file: {file}")

 
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])


    df['Month'] = df['Timestamp'].dt.month
    df['Hour'] = df['Timestamp'].dt.hour

  
    for col in columns_to_plot:
        if col in df.columns:
            plt.figure(figsize=(10, 6))
            monthly_data = df.groupby('Month')[col].mean()
            sns.barplot(x=monthly_data.index, y=monthly_data.values, palette='viridis')
            plt.title(f"Monthly Average {col} for {file}")
            plt.xlabel("Month")
            plt.ylabel(col)
            plt.xticks(range(12), [
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
            ])
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.savefig(f"monthly_{col}_{file.split('.')[0]}.png")
            plt.show()

 
    for col in columns_to_plot:
        if col in df.columns:
            plt.figure(figsize=(10, 6))
            hourly_data = df.groupby('Hour')[col].mean()
            sns.lineplot(x=hourly_data.index, y=hourly_data.values, marker='o')
            plt.title(f"Hourly Average {col} for {file}")
            plt.xlabel("Hour of Day")
            plt.ylabel(col)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.savefig(f"hourly_{col}_{file.split('.')[0]}.png")
            plt.show()

    print(f"Plots saved for file: {file}")