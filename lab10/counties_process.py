'''task 10_2'''


import pandas as pd
import doctest


def read_data(path_to_file):
    '''
    Return a dataFrame.
    '''
    df = pd.read_csv(path_to_file)
    return df

read_data('census.csv')


def max_counties(df):
    '''
    Return a string with division.
    >>> print(max_counties(read_data('census.csv')))
    Texas
    '''
    df = df[df['SUMLEV'] != 40]
    df = df.groupby('STNAME').count().nlargest(1, 'DIVISION')
    return df.index[0]

print(max_counties(read_data('census.csv')))


def max_min(df):
    '''
    Return a new dataFrame with two new lines.
    '''
    data = df[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012',
               'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']]
    df['max'] = max(data)
    df['min'] = min(data)
    return df


helper = read_data('census.csv').apply(max_min, axis=1)


def max_difference(df):
    '''
    Return a string with the right division. 
    >>> print(max_difference(read_data('census.csv')))
    Harris County
    '''
    global helper
    df = helper[helper['SUMLEV'] != 40]
    df = df[['STNAME', 'CTYNAME', 'POPESTIMATE2010', 'POPESTIMATE2011',
             'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014',
             'POPESTIMATE2015', 'max', 'min']]
    df = df.loc[abs(df['max'] - df['min']).idxmax()]
    return df[1]

print(max_difference(read_data('census.csv')))


def conditional_counties(df):
    '''
    Return 5x2 dataFrame with right city names.
    >>> print(conditional_counties(read_data('census.csv')))
             STNAME            CTYNAME
    0          Iowa  Washington County
    1     Minnesota  Washington County
    2  Pennsylvania  Washington County
    3  Rhode Island  Washington County
    4     Wisconsin  Washington County
    '''
    df = df[(df['REGION'] != 3) & (df['REGION'] != 4)]
    df = df.loc[df['CTYNAME'].str.contains('Washington')]
    df = df[df['POPESTIMATE2015'] > df['POPESTIMATE2014']]
    df = df[['STNAME', 'CTYNAME']]
    df = df.set_index(pd.Index([0, 1, 2, 3, 4]))
    return df

print(conditional_counties(read_data('census.csv')))

if __name__ == '__main__':
    print(doctest.testmod())