"""
Adapted from Code that goes along with the Airflow tutorial located at:
https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/tutorial.py


"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta



import pandas as pd
import os 




def process_dataframe(df):
    """
    1. Delete any rows where 'name' is null
    reduces number of rows to process in next steps
    df = df.dropna(subset=['name'])
    2. Split the 'name' column into two columns 
    Assume convention where first_name is in first part of string
    """
    df[['first_name','last_name']] = df['name'].str.split(' ', expand=True)
    
    # 3. Strip any '0's from the 'price' column
    df['price'] = df['price'].str.lstrip('0')

    # 4. Create a new column 'price_100' with 1 if 'price' > 100, else 0
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['above_100'] = df['price'].apply(lambda x: True if x > 100 else False)
    
    return df

def main():
    """
    Gets folder path for all files and performs process_dataframe on them
    """
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
        print(f'file: {file} processed')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),

}

with DAG(
    dag_id="process_dataframe",
    schedule='* * * * *' ,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["pandas_transformation"],
) as dag:
    # With the PythonOperator you can run a python function.
    save_date_task = PythonOperator(
        task_id='main',
        python_callable=main,
        dag=dag
    )






