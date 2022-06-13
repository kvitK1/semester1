""" TASK """

def find_max_1(f, points):
    """
    (function or str, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> print(find_max_1('x ** 2 + x', [1, 2, 3, -1]))
    12
    >>> print(find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1]))
    12
    >>> print(find_max_1('5/x + x', [1, 3, 5, 0]))
    You can`t divide by zero!
    >>> print(find_max_1(lambda x: x * (x**0.5)+ 2*x, [1, 2, 3, 4.2]))
    17.007438643406065
    """
    try:
        results_list = []
        if type(f) == str:
            for number in points:
                x = number
                results_list.append(eval(f))
            return max(results_list)

        else:
            results_list = [f(num) for num in points]
            return max(results_list)     
    except ZeroDivisionError:
        return 'You can`t divide by zero!'

find_max_1('5/x + x', [1, 3, 5, 0])
find_max_1(lambda x: x * (x**0.5)+ 2*x, [1, 2, 3, 4.2])

def find_max_2(f, points):
    """ 
    (function or str, list(number)) -> (number)

    Find and return list of points where function f has the maximal value.

    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    >>> print(find_max_2(lambda x: x ** 2, [1, 2, 3, -3, -1]))
    [3, -3]
    >>> print(find_max_2('(x ** 2)/(x-1)', [1, 2, 0, -1]))
    You can`t divide by zero!
    >>> print(find_max_2('(x ** 2)/(x-1)', [-2.5, 10, 1.5]))
    [10]
    >>> print(find_max_2(lambda x: (x ** 2)/(x-1), []))
    []
    """
    try:
        tuples_list = []
        number_list = []
        if type(f) == str:
            for number in points:
                x = number
                tuples_list.append((number, eval(f))), number_list.append(eval(f))
            results_list = [pair_tuple[0] for pair_tuple in tuples_list if pair_tuple[1] == max(number_list)]
            return results_list

        else:
            number_list = [f(num) for num in points]
            tuples_list = [(num, f(num)) for num in points]
            results_list = [pair_tuple[0] for pair_tuple in tuples_list if pair_tuple[1] == max(number_list)]
            return results_list
    except ZeroDivisionError:
        return 'You can`t divide by zero!'

find_max_2(lambda x: (x ** 2)/(x-1), [])

def compute_limit(seq):
    """
    (function or str) -> (number)
    
    Compute and return limit of a convergent sequence.
    
    >>> print(compute_limit('(n ** 2 + n) / n ** 2'))
    1.0
    >>> print(compute_limit(lambda n: (n ** 2 + n) / n ** 2))
    1.0
    >>> print(compute_limit('(3 * (n**2) + 1) / (5 * (n**2) - 1)'))
    0.6
    >>> print(compute_limit(lambda n: (n + 2)/(3*n -1)))
    0.33
    >>> print(compute_limit('(7*(n**2) + 7*n - 2)/(n**2 - 2*n +3)'))
    7.0
    """
    if type(seq) == str:
        lst = []
        i = 0
        while True:
            n = 10 ** i
            lst.append(eval(seq))
            if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:  
                return round(lst[i], 2)
                break
            i += 1
    else:
        lst = []
        i = 0
        while True:
            k = seq(10**i)
            lst.append(k)
            if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:  
                return round(lst[i], 2)
                break
            i += 1

compute_limit(lambda n: (n ** 2 + n) / n ** 2)
compute_limit('(3 * (n**2) + 1) / (5 * (n**2) - 1)')
compute_limit(lambda n: (n + 2)/(3*n -1))
compute_limit('(7*(n**2) + 7*n - 2)/(n**2 - 2*n +3)')

def compute_derivative(f, x_0):
    """
    (function or str, number) -> (number)
    
    Compute and return derivative of function f in the point x_0.
    
    >>> compute_derivative('x ** 2 + x', 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    pass

def get_tangent(f, x_0):
    """
    (function or str, number) -> (str)
    
    Compute and return tangent line to function f in the point x_0.
    
    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '- 3.0 * x - 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x - 4.0'
    """
    pass

def get_root(f, a, b):
    """
    (function or str, number, number) -> (number)
    
    Compute and return root of the function f in the interval (a, b).
    
    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    pass