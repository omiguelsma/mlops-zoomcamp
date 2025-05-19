import pandas as pd

def compute_duration(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Função para calcular a duração em minutos entre as colunas
    'tpep_dropoff_datetime' e 'tpep_pickup_datetime' de um DataFrame.

    Args:
        dataframe (pd.DataFrame): O DataFrame de entrada contendo as colunas de data/hora.

    Returns:
        pd.DataFrame: O DataFrame com uma nova coluna 'duration' em minutos.

    Raises:
        KeyError: Se as colunas 'tpep_dropoff_datetime' ou 'tpep_pickup_datetime' não existirem.
        TypeError: Se as colunas de data/hora não forem do tipo datetime.
    """
    # É uma boa prática garantir que as colunas são do tipo datetime
    # antes de realizar operações de subtração de tempo.
    # No entanto, se você já as converteu anteriormente (ex: ao carregar os dados),
    # essas linhas podem ser removidas para evitar processamento redundante.
    if not pd.api.types.is_datetime64_any_dtype(dataframe['tpep_dropoff_datetime']):
        dataframe['tpep_dropoff_datetime'] = pd.to_datetime(dataframe['tpep_dropoff_datetime'])
    if not pd.api.types.is_datetime64_any_dtype(dataframe['tpep_pickup_datetime']):
        dataframe['tpep_pickup_datetime'] = pd.to_datetime(dataframe['tpep_pickup_datetime'])

    dataframe['duration'] = (dataframe['tpep_dropoff_datetime'] - dataframe['tpep_pickup_datetime']).dt.total_seconds() / 60

    return dataframe