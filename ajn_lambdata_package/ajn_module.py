def check_nulls(df):
    return(df.isnull().sum().sort_values())

def add_col(df, new_list, colname):
    df[colname] = pd.Series(new_list)
    return df
