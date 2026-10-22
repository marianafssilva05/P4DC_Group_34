
def most_connected(df, ftype):
    filtered = df[df["strength"] == ftype] # filter the pokemon dataset by ftype
    top_pok = filtered["Name_friend1"].value_counts().index[0] # rank and find the first
    return f'{top_pok} has most {ftype}'
    
