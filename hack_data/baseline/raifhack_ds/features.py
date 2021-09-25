import pandas as pd
from .utils import UNKNOWN_VALUE

def prepare_categorical(df: pd.DataFrame) -> pd.DataFrame:
    """
    Заполняет пропущенные категориальные переменные
    :param df: dataframe, обучающая выборка
    :return: dataframe
    """
    df_new = df.copy()
    fillna_cols = ['region','city','street','realty_type']
    df_new[fillna_cols] = df_new[fillna_cols].fillna(UNKNOWN_VALUE)
    return df_new


def parse_date(df, col='date'):
    df[col] = pd.to_datetime(df[col])
    df['month'] = df[col].dt.month
    df['dayofmonth'] = df[col].dt.day
    df['dayofweek'] = df[col].dt.dayofweek
    df['dayofyear'] = df[col].dt.dayofyear

    return df

