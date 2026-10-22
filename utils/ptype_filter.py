
def ptype_filter(df, ptype="Normal"):
    df = df.copy()
    # Your code goes here
    return df[df["Type_Full"].str.contains(ptype)]
