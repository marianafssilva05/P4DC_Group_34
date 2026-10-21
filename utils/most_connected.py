
def most_connected(df, ftype):
    # Your code goes here
    rank = df[df["strength"] == ftype]["friend1"].value_counts()
    print(f'{df[df["friend1"] == rank.index[0]]["Name_friend1"].max()} has most {ftype}')
    return
