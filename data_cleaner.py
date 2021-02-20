import pandas as pd
import sys
import re

def clean_csv(file):
    df = pd.read_csv(file, sep=',')
    drop_list = []
    for key in df.keys():
        if key[:7] == 'Unnamed':
            drop_list.append(key)

        try:
            df[key] = df[key].astype(int)

        except ValueError:
            continue

    df.drop(columns=drop_list, inplace=True)
    df.dropna(axis=0, how='all', inplace=True)
    df.reset_index(inplace=True)
    return df