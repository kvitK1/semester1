'''
task 10_1 
'''
import doctest
import pandas as pd
# import numpy as np

def read_data():
    '''
    A function to read csv files.
    Return a table with data.
    '''
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            df.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = df.index.str.split('\\s\\(') # split the index by '('

    df.index = names_ids.str[0]  # the [0] element is the country name (new index)
    df['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or I
    # D (take first 3 characters from that)

    df = df.drop('Totals')
    return df
    # print(df)

# print(read_data())

def first_country(df):
    '''
    Return pandas Series with the first country in the table.
    >>> print(first_country(read_data()))
    # Summer           13
    Gold                0
    Silver              0
    Bronze              2
    Total               2
    # Winter            0
    Gold.1              0
    Silver.1            0
    Bronze.1            0
    Total.1             0
    # Games            13
    Gold.2              0
    Silver.2            0
    Bronze.2            2
    Combined total      2
    ID                AFG
    Name: Afghanistan, dtype: object
    '''
    ds = df.iloc[0]
    return ds

# print(first_country(read_data()))


def summer_biggest(df):
    '''
    Return string with the right counry.
    >>> print(summer_biggest(read_data()))
    United States
    '''
    max_medals = df.loc[df['Gold'].idxmax()]
    return df['Gold'].idxmax()

print(summer_biggest(read_data()))


def difference_biggest(df):
    '''
    Return string with the right country.
    >>> print(difference_biggest(read_data()))
    United States
    '''
    diff = abs(df['Gold'] - df['Gold.1']).idxmax()
    return diff

print(difference_biggest(read_data()))


def difference_biggest_relative(df):
    '''
    Return a string with the right country.
    >>> print(difference_biggest_relative(read_data()))
    Bulgaria
    '''
    df.loc[
    (df['Gold'] != 0) & (df['Gold.1'] != 0), 
    'new_column'] = abs((df['Gold'] - df['Gold.1'])/df['Gold.2'])
    diff = df.loc[df['new_column'].idxmax()]
    return diff.name

# print(difference_biggest_relative(read_data()))


def get_points(df):
    '''
    Return a column in dataFrame as pandas Series.
    >>> print(get_points(read_data()))
    Afghanistan                           2
    Algeria                              27
    Argentina                           130
    Armenia                              16
    Australasia                          22
                                       ... 
    Yugoslavia                          171
    Independent Olympic Participants      4
    Zambia                                3
    Zimbabwe                             18
    Mixed team                           38
    Name: Points, Length: 146, dtype: int64
    '''
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']
    ds = df['Points']
    return ds

# if __name__ == "__main__":
    doctest.testmod()