#!/usr/bin/env python
# coding: utf-8

import os
import argparse

from time import time

from datetime import timedelta

import pandas as pd
from sqlalchemy import create_engine
from prefect import flow, task
from prefect.tasks import task_input_hash
from prefect_sqlalchemy import SqlAlchemyConnector


@task(
    log_prints=True,
    tags=["extract"],
    cache_key_fn=task_input_hash,
    cache_expiration=timedelta(days=1),
)
def extract_data(filename, raw_folder_path):
    schema = {
    'name': 'string',
    'price': 'string'
    }


    df = pd.read_csv(f"{raw_folder_path}/{filename}", dtype=schema )
    return df



@task(log_prints=True)
def transform_data(df):
    
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



@task(log_prints=True, retries=3)
def load_data(processed_df, processed_folder_path, file):

    processed_df.to_csv(f"{processed_folder_path}/processed_{file}", index=False)  


@flow(name="Subflow", log_prints=True)



@flow(name="Data transformation", timeout_seconds=120)
def main(filename):
    # Define the folder path
    raw_folder_path = 'Datasets'
    processed_folder_path = 'Processed_Datasets'

    raw_data = extract_data(filename, raw_folder_path)
    processed_df = transform_data(raw_data)
    load_data(processed_df, processed_folder_path, filename)


if __name__ == "__main__":
    main("dataset1.py")

