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


def uncode_street(df):

    def parse_street(value):
        if value=='missing':
            return -1
        else:
            return int(str(value)[1:])

    df['street_num'] = df['street'].apply(lambda x: parse_street(x))

    return df

