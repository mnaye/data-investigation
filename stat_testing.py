#For running statistical test, such as chi-squared test
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def chi_clean(index_field, column_field):
    '''This function takes two fields, makes a cross tabulation data frame, and removes rows with less than five row totals
       index_field: independent variable serving as indexes for the cross tab data frame
       column_field: dependent variable serving as columns for the cross tab data frame
       return: a cross tab data frame with row totals more than five without column and row totals
    '''
    df = pd.crosstab(index=index_field, columns=column_field, margins=True)

    # Getting a list of names for the indexes
    index_list = []
    for i in index_field.unique():
        index_list.append(i)

    index_list = sorted(index_list)
    index_list.append("coltotal")
    df.index = index_list

    # Getting a list of names for columns
    col_list = []
    for i in column_field.unique():
        col_list.append(i)

    col_list = sorted(col_list)
    col_list.append("rowtotal")
    df.columns = col_list

    # Dropping the row with column total
    df = df.drop(df.index[-1])

    # Removing rows with less than rowtotal of five
    df = df[df["rowtotal"] > 5]

    # Dropping the rowtotal column
    df = df.drop("rowtotal", 1)

    return df

def chi_test(indepedent_var, dependent_var, description):
    '''This function performs a chi squared test and indicates its statistical significance
       indepedent_var: independent variable-condition
       dependent_var: dependent variable
       description:  description of the variables in string format
       return: description, pvalue, and status of statistical significance
    '''
    con_table = chi_clean(indepedent_var,
                          dependent_var)  # Calling chi clean to remove records with totals of less than five
    chisq_value, pvalue, df, expected = chi2_contingency(con_table)
    if pvalue < 0.05:
        return description + " IS statistically sigificant at " + str('{0:f}'.format(pvalue)) + "."

    if pvalue >= 0.05:
        return description + " IS NOT statistically sigificant at " + str('{0:f}'.format(pvalue)) + "."
