
def column_splitter(
                    df, 
                    col="Type_Full", 
                    sep="_", 
                    new_col="Type_Full_List"
                    ):
    df[new_col] = df[col].str.split(sep)

def type_comparer(df):
    qualities = ["HP", "Attack", "Defense", "SpAtk", "SpDef", "Speed"]
    exploded_df = df.explode("Type_Full_List")
    return exploded_df.groupby("Type_Full_List")[qualities].mean()
