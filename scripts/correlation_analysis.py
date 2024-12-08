import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


data_folder = '../data'


csv_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]


for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
    print(f"Processing file: {file}")
    
  
    relevant_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
    relevant_columns = [col for col in relevant_columns if col in df.columns]
    
    if not relevant_columns:
        print(f"No relevant columns found in {file}. Skipping.")
        continue


    correlation_matrix = df[relevant_columns].corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)


    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title(f"Correlation Matrix for {file}")
    plt.tight_layout()
    plt.savefig(f"correlation_matrix_{file.split('.')[0]}.png")
    plt.show()

  
    sns.pairplot(df[relevant_columns], diag_kind="kde", corner=True, plot_kws={'alpha': 0.6})
    plt.suptitle(f"Pair Plot for {file}", y=1.02)
    plt.savefig(f"pair_plot_{file.split('.')[0]}.png")
    plt.show()

    print(f"Correlation analysis completed for file: {file}")
