#For visualizing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_seaborn_pair(df, field, file_name):
    '''This function takes in:
            df as a data frame,
            field as the column of the data frame,
            and a file name in quotation marks
        and makes a seaborn pair plot and saves the image of the plot in file_name'''
    #% matplotlib inline
    plt.figure()
    p = sns.pairplot(data=df, hue=field, dropna=True, palette="husl")
    p.fig.text(0.33, 1.02, "A High-Level View of Relationship Between Variables", fontsize=20)
    plt.savefig(file_name)


def make_corr_matrix(df, file_name):
    ''' This function makes a correlation matrix with shades of red.  Floats and integers are formmated
        to fit in the matrix.
        df: data frame
        file_name:  file name to be saved
    '''
    #% matplotlib inline
    correlation = df.corr().round(2)

    # Generate a mask for the upper triangle
    mask = np.zeros_like(correlation, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    setting = "g"
    plt.figure()
    sns.heatmap(correlation, mask=mask, annot=True, cmap='Reds', fmt=setting, linewidths=.5)
    plt.title("Correlations Between Variables", fontsize=20)
    plt.savefig(file_name)


def make_boxplot(df, y, x, file_name):
    '''This function makes a box plot
       df: data frame
       y: field for y axis
       x: field for x axis
       file_name: file name to be saved
    '''
    #% matplotlib inline
    plt.figure()
    sns.boxplot(x=x, y=y, data=df)
    plt.xlabel(str(x), fontsize=16)
    plt.ylabel(str(y), fontsize=16)
    plt.title("Distributions of " + str(y) + " by " + str(x), fontsize=20)
    plt.savefig(file_name)


def make_barchart(field1, field2, field3):
    '''This function makes a bar chart based on three variables
       field1:  variable 1
       field2: variable 2
       field3:  grouping variable
       group_labels:  labels for the x ticks
    '''
    cat_groups = pd.crosstab([field1, field2], field3.astype(bool)).apply(lambda r: r / r.sum(), axis=1)
    ax = cat_groups.plot(kind='bar', stacked=False, color=["red", "green"], grid=False)
    ax.set_ylabel("Proportion")
    ax.set_title("Comparison Of " + str(field3.name) + " By " + str(field1.name) + " And " + str(field2.name))