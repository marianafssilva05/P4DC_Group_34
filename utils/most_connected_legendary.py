
def most_connected_legendary(df, ftype):
    # Your code goes here
    filtered = df[(df["strength"] == ftype) & (df["Legendary_friend2"] == True)]
    top_pokemon = filtered["Name_friend1"].value_counts().index[0]
    return f"{top_pokemon} has most {ftype}"
