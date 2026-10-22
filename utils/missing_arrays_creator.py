import pandas as pd
import numpy as np

def missing_bool(df, col="Legendary"):
    return df[col].isna()

def missing_arrays_creator(
        df, 
        missing, 
        features=("HP", "Attack", "Defense", "SpAtk", "SpDef", "Speed")
        ):

    values_missing = df.loc[missing, list(features)].values
    values_known = df.loc[~missing, list(features)].values

    min_value = df[list(features)].min().values
    max_value = df[list(features)].max().values

    values_missing = (values_missing - min_value) / (max_value - min_value)
    values_known = (values_known - min_value) / (max_value - min_value)
    
    return values_missing, values_known
