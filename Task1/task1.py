import pandas as pd
import os 

def process_dataframe(df):

    # 1. Delete any rows where 'name' is null
    # reduces number of rows to process in next steps
    df = df.dropna(subset=['name'])
    # 2. Split the 'name' column into two columns 
    # Assume convention where first_name is in first part of string

    df[['first_name','last_name']] = df['name'].str.split(' ', expand=True)
    
    # 3. Strip any '0's from the 'price' column
    df['price'] = df['price'].str.lstrip('0')

    
    

    
    # 4. Create a new column 'price_100' with 1 if 'price' > 100, else 0
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['above_100'] = df['price'].apply(lambda x: True if x > 100 else False)
    
    return df

if __name__ == "__main__":
    schema = {
    'name': 'string',
    'price': 'string'
    }
    # Define the folder path
    raw_folder_path = 'Datasets'
    processed_folder_path = 'Processed_Datasets'
    # Get the list of filenames
    filenames = [filename for filename in os.listdir(raw_folder_path) if os.path.isfile(os.path.join(raw_folder_path, filename))]
    for file in filenames:
        df = pd.read_csv(f"{raw_folder_path}/{file}", dtype=schema )
        processed_df = process_dataframe(df)
        processed_df.to_csv(f"{processed_folder_path}/processed_{file}", index=False)
