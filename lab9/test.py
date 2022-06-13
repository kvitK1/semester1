""" task 9_2 """
def find_max_1(func, points):
    """
    (function or str, list(number)) -> (number)
    Find and return maximal value of function f in points.
    >>> print(find_max_1('x ** 2 + x', [1, 2, 3, -1]))
    12
    >>> print(find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1]))
    12
    >>> print(find_max_1(lambda x: x * (x**0.5)+ 2*x, [1, 2, 3, 4.2]))
    17.007438643406065
    """
    results_list = []
    if isinstance(func, str):
        for number in points:
            x = number
            results_list.append(eval(func))
        return max(results_list)
    else:
        results_list = [func(num) for num in points]
        return max(results_list)

def find_max_2(func, points):
    """
    (function or str, list(number)) -> (number)
    Find and return list of points where function f has the maximal value.
    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    >>> print(find_max_2(lambda x: x ** 2, [1, 2, 3, -3, -1]))
    [3, -3]
    >>> print(find_max_2('(x ** 2)/(x-1)', [-2.5, 10, 1.5]))
    [10]
    >>> print(find_max_2(lambda x: (x ** 2)/(x-1), []))
    []
    """
    tuples_list = []
    number_list = []
    if isinstance(func, str):
        for number in points:
            x = number
            tuples_list.append((number, eval(func))), number_list.append(eval(func))
        results_list = [pair_tuple[0] for pair_tuple in tuples_list if pair_tuple[1] == max(number_list)]
        return results_list
    else:
        number_list = [func(num) for num in points]
        tuples_list = [(num, func(num)) for num in points]
        results_list = [pair_tuple[0] for pair_tuple in tuples_list if pair_tuple[1] == max(number_list)]
        return results_list

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
    if isinstance(seq, str):
        lst = []
        count = 0
        while True:
            n = 10 ** count
            lst.append(eval(seq))
            if count != 0 and abs(lst[count] - lst[count - 1]) < 0.001:
                return round(lst[count], 2)
            count += 1
    else:
        lst = []
        count = 0
        while True:
            new_seq = seq(10**count)
            lst.append(new_seq)
            if count != 0 and abs(lst[count] - lst[count - 1]) < 0.001:
                return round(lst[count], 2)
            count += 1

def compute_derivative(func, x_0):
    """
    (function or str, number) -> (number)
    Compute and return derivative of function f in the point x_0.
    >>> print(compute_derivative('x ** 2 + x', 2))
    5.0
    >>> print(compute_derivative(lambda x: x ** 2 + x, 2))
    5.0
    >>> print(compute_derivative('x**3 + x**2', 4))
    56.0
    """
    aprox = []
    count = 0
    while True:
        x = x_0 + 10**(-count)
        d_f = (eval(func) if isinstance(func, str) else func(x))
        x = x_0
        d_f -= (eval(func) if isinstance(func, str) else func(x))
        der = d_f / 10**(-count)
        aprox.append(der)
        if count != 0 and abs(aprox[count] - aprox[count - 1]) < 0.001:  
            return round(aprox[count], 2)
        count += 1

def get_tangent(func, varb):
    """
    (function or str, number) -> (str)
    Compute and return tangent line to function f in the point x_0.
    >>> get_tangent('x ** 2 + x', 2)
    5.0 * x - 4.0
    >>> get_tangent('- x ** 2 + x', 2)
    - 3.0 * x + 4.0
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    5.0 * x - 4.0
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    - 3.0 * x + 4.0
    """
    pochidna = compute_derivative(func, varb)
    x = varb
    fun_in_point = round(float((eval(func) if isinstance(func, str) else func(x))), 2)
    coefficient = pochidna * (-varb) + fun_in_point
    if coefficient < 0:
        coefficient = str(coefficient)
        coef = coefficient[:1] + " " + coefficient[1:]
    else:
        coef = "+ {}".format(coefficient)
    if pochidna < 0:
        pochidna = str(pochidna)
        pochidna = pochidna[:1] + " " + pochidna[1:]
    else:
        pochidna = str(pochidna)
    new_string = pochidna + " * x " + coef    # "\'\'"
    return new_string

def get_root(func, a_coef, b_coef):
    """
    (function or str, number, number) -> (number)
    Compute and return root of the function f in the interval (a, b).
    >>> print(get_root('x', -1, 1))
    0.0
    >>> print(get_root(lambda x: x, -1, 1))
    0.0
    >>> print(get_root("x - 7", -3, 7))
    7.0
    >>> print(get_root(lambda x: x**2 - 4, -3, 1))
    -2.0
    """
    # if type(func) == str:
    #     start_x = a_coef
    #     while True:
    #         res = eval(func, {"x": start_x})
    #         if round(res, 2) == 0:
    #             tot = round(start_x, 2)
    #             if tot == -0:
    #                 return abs(tot)
    #             return tot
    #         start_x += 0.001
    # else:
    start_x = a_coef
    while True:
        x=start_x
        res = (eval(func) if isinstance(func, str) else func(start_x))
        if round(res, 2) == 0:
            tot = round(start_x, 2)
            if tot == -0:
                return abs(tot)
            return tot
        start_x += 0.001
    # lasts_list = [a_coef, b_coef]
    # for i in lasts_list:
    #     x = i
    #     if (eval(func) if isinstance(func, str) else func(x)) == 0:
    #         return round(float(x), 2)
    # while (eval(func) if isinstance(func, str) else func(x)) != 0:
    #     mid = (a_coef+b_coef)/2
    #     x = mid
    #     result = (eval(func) if isinstance(func, str) else func(x))
    #     if result < 0:
    #         b_coef = mid
    #     else:
    #         a_coef = mid
    # return round(float(x), 2)

print(get_root('x**2 - 4', -3, 1))
print(get_root(lambda x: x**3 - 8, -9, 2))
print(get_root(lambda x: x - 7, -3, 7))
print(get_root('x', -1, 1))
print(get_root(lambda x: x**2 - 4, -3, 1))
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
