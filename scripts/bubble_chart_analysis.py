import pandas as pd
import os
import matplotlib.pyplot as plt


data_folder = '../data'


csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]


def create_bubble_chart(df, x_col, y_col, size_col, title, output_file):
    plt.figure(figsize=(10, 6))

    plt.scatter(df[x_col], df[y_col], s=df[size_col] * 10, alpha=0.6, edgecolors="w", linewidth=0.5)
    
  
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    

    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
    print(f"Processing file: {file}")
    

    relevant_columns = ['GHI', 'Tamb', 'WS', 'RH', 'BP']
    relevant_columns = [col for col in relevant_columns if col in df.columns]
    
  
    df = df[relevant_columns].dropna()
    

    x_col = 'GHI'
    y_col = 'Tamb'
    size_col = 'RH' 
    
 
    title = f"Bubble Chart: {x_col} vs {y_col} vs {size_col} ({file})"
    output_file = f"bubble_chart_{file.split('.')[0]}.png"
    create_bubble_chart(df, x_col, y_col, size_col, title, output_file)
    
    print(f"Bubble chart saved as: {output_file}")
