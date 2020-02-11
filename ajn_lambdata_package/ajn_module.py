import pandas as pd


def check_nulls(df):
    """
    Takes a data frame and returns a sorted list of the number
    of null values each column has.
    """
    return(df.isnull().sum().sort_values())

def add_col(df, new_list, colname):
    """
    Adds a user-provided list as a column to a user-provided data frame.

    Takes three arguments: the data frame, the list to be appended, and
    the name of the new column. Converts the list into a series, then
    defines a new column by the column name as the list-based series.

    Params:

        df (data frame): the data frame to be added to
        new_list (list): the list you want to append to the df
        colname (string): what you want to name the column
    """
    df[colname] = pd.Series(new_list)
    return df

class RawDF(object):
    def __init__(self, df):
        self.df = df

    def add_col_class(self, new_list, colname):
        self.df[colname] = pd.Series(new_list)
