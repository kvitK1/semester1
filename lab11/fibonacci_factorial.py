'''module with iter. and recur. funcs to count Fibonacci and factorial'''


from time import time


def factorial_recursive(num):
    """
    Returns a factorial of the num recursively.
    >>> print(factorial_recursive(5))
    120
    >>> print(factorial_recursive(0))
    1
    >>> print(factorial_recursive(8))
    40320
    """
    if num == 0:
        return 1
    else:
        return num * factorial_recursive(num-1)


def factorial_iterative(num):
    """
    Returns a factorial of the num iteratively.
    >>> print(factorial_iterative(5))
    120
    >>> print(factorial_iterative(0))
    1
    >>> print(factorial_iterative(8))
    40320
    """
    i = 0
    number = 1
    while i != num:
        number *= (num-i)
        i += 1
    return number


def fibonacci_recursive(num):
    """
    Returns Fibonacci number of num index.
    >>> print(fibonacci_recursive(0))
    1
    >>> print(fibonacci_recursive(5))
    8
    >>> print(fibonacci_recursive(7))
    21
    >>> print(fibonacci_recursive(12))
    233
    """
    if num <= 1:
        return 1
    else:
        return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)


def fibonacci_iterative(num):
    """
    Returns Fibonacci number of num index.
    >>> print(fibonacci_recursive(0))
    1
    >>> print(fibonacci_recursive(5))
    8
    >>> print(fibonacci_recursive(7))
    21
    >>> print(fibonacci_recursive(12))
    233
    """
    curr = 1
    prev = 1
    for _ in range(num - 1):
        curr, prev = curr + prev, curr
    return curr


def numbers_time_test(function=0, realisation=0):
    """
    Func to get info about previous functions.
    """
    start_time = time()
    if function == 0:
        if realisation == 0:
            factorial_recursive(6)
            results = time()-start_time
            return results
        elif realisation == 1:
            factorial_iterative(6)
            results = time()-start_time
            return results
    elif function == 1:
        if realisation == 0:
            fibonacci_recursive(6)
            results = time()-start_time
            return results
        elif realisation == 1:
            fibonacci_iterative(6)
            results = time()-start_time
            return results
