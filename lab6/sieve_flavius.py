def sieve_flavius(n: int):
    """
    Returns the list of lucky numbers.
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []

    """
    num_lst = [i for i in range(1, n + 1)]

    for elemn in num_lst:
        if elemn%2 == 0:
            num_lst.remove(elemn)

    i = 1
    while i < len(num_lst):
        k = num_lst[i]
        del num_lst[k-1::k]
        i += 1
    
    return num_lst

sieve_flavius()

import doctest
print(doctest.testmod())