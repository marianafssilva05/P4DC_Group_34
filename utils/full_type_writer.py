
def full_type_writer(df):
    df = df.copy()
    df["Type_Full"] = df["Type1"]
    df.loc[df["Type2"].notna(), "Type_Full"] += "_" + df["Type2"]
    return df
