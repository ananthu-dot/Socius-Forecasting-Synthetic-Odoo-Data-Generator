import pandas as pd


# Normalize column names in a pandas DataFrame
@staticmethod
def normalize_column_names(df):

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
    )

    return df
