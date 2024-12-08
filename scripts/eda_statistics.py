import pandas as pd
import os


data_folder = '../data'

csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]

for file in csv_files:

    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
  


    print("=====================================================")
    print(f"Processing file: {file}")  
    print("dataset Information:")
    print(df.info())

    numeric_columns = df.select_dtypes(include= ['float64', 'int64']).columns
    print(f"Number of numeric colums: {len(numeric_columns)}")
    print(f"Numeric columns are: {list(numeric_columns)}")
    
    summary_stats= df[numeric_columns].describe().T
    summary_stats['median']= df[numeric_columns].median()
    
    print("\nSummary Statistics:")
    print(summary_stats)
    
    
    output_file = f'summary_statistics_{file.replace(".csv", "")}.csv'
    summary_stats.to_csv(output_file, index=True)
    print(f"Summary statistics saved to {output_file}")
    print("=====================================================")


