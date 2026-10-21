
def mega_cleaner(df):
    df = df.copy()
    # Your code goes here
    df["Name"] = df["Name"].apply(lambda x: x[x.find("Mega "):] if "Mega " in x else x)
    return df
