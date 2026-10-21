import pandas as pd

def friend_merger(
        friends,
        df,
        cols_to_keep=("Name", "Generation", "Legendary", "Type_Full")
):
    # Your code goes here
    friends_cols = list(friends.columns)
    cols_friend1 = {col: col + "_friend1" for col in cols_to_keep} # dict to rename the columns
    cols_friend2 = {col: col + "_friend2" for col in cols_to_keep}

    result = pd.merge(friends, df, how="left", left_on="friend1", right_on="Num")[friends_cols + list(cols_to_keep)].rename(columns=cols_friend1)
    result_cols = list(result.columns)
    result = pd.merge(result, df, how="left", left_on="friend2", right_on="Num")[result_cols + list(cols_to_keep)].rename(columns=cols_friend2)
    return result
