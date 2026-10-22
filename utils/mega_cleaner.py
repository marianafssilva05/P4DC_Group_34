
def mega_cleaner(df):
    df = df.copy()
    # removes any text that appears before “Mega ”
    df["Name"] = df["Name"].apply(lambda x: x[x.find("Mega "):] if "Mega " in x else x)
    return df
