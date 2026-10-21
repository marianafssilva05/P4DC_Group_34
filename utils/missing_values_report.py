
def missing_values_report(df):
    missing_counts = df.isna().sum() # the number of missing values per column

    return missing_counts[missing_counts > 0].to_dict() # filter columns with missing values > 0 and convert to a dictionary
