import pandas as pd

def cast_metrics(dataframe: pd.DataFrame) -> pd.DataFrame:
    "Function to cast metrics"
    categorical = ['PULocationID', 'DOLocationID']
    dataframe[categorical] = dataframe[categorical].astype('str')
    return dataframe