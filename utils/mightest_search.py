
def mightest_search(df, metric="HP"):
    #Sorts the DataFrame by the selected metric in ascending order and returns the name of the Pokémon with the highest value
    sorted_df = df.sort_values(by=metric, ascending=False)
    return sorted_df["Name"].iloc[0]
