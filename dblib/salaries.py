import pandas as pd
import dask.dataframe as dd
def load_data(dataset = 'datasets/ds_salaries.csv'):
    """Load the salaries dataset from the data folder to a pandas dataframe"""
    df = pd.read_csv(dataset)
    return df

def load_data_dask(dataset = 'datasets/ds_salaries.csv'):
    """Load the salaries dataset from the data folder to a dask dataframe"""
    df = dd.read_csv(dataset, blocksize=None)
    return df
