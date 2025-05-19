import pandas as pd


def select_metrics(dataframe: pd.DataFrame) -> pd.DataFrame:
    "Function to select metrics"
    # Definition of metrics
    categorical = ['PULocationID', 'DOLocationID'] #['PU_DO',]
    numerical = ['trip_distance',]
    
    # Join metrics
    dataframe['PU_DO'] = dataframe['PULocationID'] + '_' + dataframe['DOLocationID']
    
    # Select variables
    filtered_df = dataframe[numerical + categorical].copy()
    
    return filtered_df