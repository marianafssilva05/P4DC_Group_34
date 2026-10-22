
# Since the column Type1 doesn't contain NaN we can start by equaling the column Type_Full to Type1
def full_type_writer(df):
    df = df.copy()
    df["Type_Full"] = df["Type1"]
    df.loc[df["Type2"].notna(), "Type_Full"] += "_" + df["Type2"]
    return df
