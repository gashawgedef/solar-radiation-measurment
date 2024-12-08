import pandas as pd
import os


data_folder = '../data'


csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]


def clean_data(df):
 
    df = df.dropna(axis=1, how='all')

 
    df['ModA'].fillna(df['ModA'].mean(), inplace=True)  
    df['ModB'].fillna(df['ModB'].mean(), inplace=True)  
    df['GHI'].fillna(df['GHI'].mean(), inplace=True)  
    df['DNI'].fillna(df['DNI'].mean(), inplace=True) 
    df['DHI'].fillna(df['DHI'].mean(), inplace=True)  
    df['Tamb'].fillna(df['Tamb'].mean(), inplace=True)  

 
    df['GHI'] = df['GHI'].apply(lambda x: max(x, 0))  
    df['DNI'] = df['DNI'].apply(lambda x: max(x, 0))  
    df['DHI'] = df['DHI'].apply(lambda x: max(x, 0))  
    df['ModA'] = df['ModA'].apply(lambda x: max(x, 0))  
    df['ModB'] = df['ModB'].apply(lambda x: max(x, 0))  
    df['Tamb'] = df['Tamb'].apply(lambda x: max(x, 0))  

 
    df = df.dropna(axis=0, subset=['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb'])

 
    if 'Comments' in df.columns:
        df = df.drop(columns=['Comments'])

    return df


for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)

    print(f"Processing file: {file}")
    
   
    cleaned_df = clean_data(df)
    
   
    cleaned_file_path = f"cleaned_{file}"
    cleaned_df.to_csv(cleaned_file_path, index=False)
    
    print(f"Cleaned dataset saved as: {cleaned_file_path}")
