
def ptype_filter(df, ptype="Normal"):
    df = df.copy()
    return df[df["Type_Full"].str.contains(ptype)] # looks for rows where Type_Full contains the string ptype
