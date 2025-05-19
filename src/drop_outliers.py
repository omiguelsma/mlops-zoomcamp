import pandas as pd

def drop_outliers(dataframe: pd.DataFrame) -> pd.DataFrame:
    "Function to drop outliers"
    return dataframe[(dataframe['duration'] >= 1) & (dataframe['duration'] <= 60)]