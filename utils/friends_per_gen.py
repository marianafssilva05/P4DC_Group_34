import pandas as pd

def friends_per_gen(df):
    # we create a Series with multiple index by grouping the dataframe and 
    # then counting the amount of legendary/not legendary friends per Generation
    grouped = df.groupby(["Generation_friend1", "Legendary_friend1"])["friend2"].nunique()
    return grouped.unstack()
