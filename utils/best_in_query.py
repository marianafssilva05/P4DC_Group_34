
def best_in_query(df, query, key):
    # Your code goes here
    filtered_df = df.query(query)
    sorted_df = filtered_df.sort_values(by=key, ascending=False)
    return sorted_df[["Name", "Type_Full"]].head(5)
