#For cleaning data
import pandas as pd
import numpy as np

def search_na(df):
    '''This function takes in a data frame and removes NAs based on user's choice
       df: data frame
       returns column names with NAs
    '''
    # Showing data frame with NAs as true
    df = df.isnull().any()
    df = df[df == True].index
    print "Here are the columns with NAs.\n", df


def search_cat(df):
    '''This function searches for categorical values
       df: data frame
       prints a list of categorical fields
    '''
    print df.select_dtypes(['object']).columns


def replace_cat(field, replacement, data_type):
    '''This function replaces a column's values in a data frame
       field: column name
       replacement: new values
       data_type:  data type of new values
       return: colum of the same name with new values
    '''
    return field.map(replacement).astype(data_type)


def fill_nan(field):
    '''This function takes a pandas series and returns a new series that fills NAs with its median if the series is numeric and
        its mode if the series is
        categorical
        field is the panda series'''
    if field.dtype == "int" or field.dtype == "float":
        return field.fillna(field.median())
    if field.dtype == "object":
        return field.fillna((field.value_counts().index[0]))
