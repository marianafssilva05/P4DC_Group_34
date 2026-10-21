import pandas as pd

def friend_merger(
        friends,
        df,
        cols_to_keep=("Name", "Generation", "Legendary", "Type_Full")
):
    # Your code goes here
    cols = list(cols_to_keep)

    # Merge attributes for friend1
    merged_f1 = pd.merge(
        friends,
        df[cols],
        left_on="friend1",
        right_index=True,
        how="left"
    )

    # Merge attributes for friend2 and apply suffixes
    merged_both = pd.merge(
        merged_f1,
        df[cols],
        left_on="friend2",
        right_index=True,
        how="left",
        suffixes=("_friend1", "_friend2")
    )
    return merged_both
