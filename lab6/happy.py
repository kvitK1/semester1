def summ(string):
    """
    string -> str
    Returns the sum of all characters in string
    """

    summa = 0
    for i in string:
        summa += int(i)
    return summa

def happy_number(num):
    """
    num -> int
    Returns True or False if the left side is equal to right side of the number
    >>> happy_number(12345)
    False
    >>> happy_number(43211234)
    True
    >>> happy_number(191234)
    True
    """

    string = str(num)
    new_string = ""
    if len(string) < 8:
        new_string = '0'*(8-len(string)) + string
    return summ(new_string[:4]) == summ(new_string[4:])

def happy_numbers(m, n):
    """
    m, n -> int
    Returns the list filled with all possible lucky numbers between m and n
    >>> happy_numbers(245, 260)
    [245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260]
    """
    lst = []
    for i in range(m, n+1):
        if happy_number(i) == True:
            lst.append(i)
    return lst

happy_numbers(245, 260)

def count_happy_numbers(n):
    """
    n -> int
    Returns the number of lucky numbers
    >>> count_happy_numbers(58990)
    125
    """

    happy_lst = 0
    for i in range(1, n+1):
        if happy_number(i) == True:
            happy_lst += 1
    return print(happy_lst)
count_happy_numbers(58990)

import doctest
print(doctest.testmod())



