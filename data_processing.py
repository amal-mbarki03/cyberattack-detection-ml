import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.dropna()
    return df

def split_features_labels(df):
    X = df.drop("label", axis=1)
    y = df["label"]
    return X, y
