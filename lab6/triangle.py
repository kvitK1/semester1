def generate_pascal_triangle(num):
    """
    int -> list
    Returns the list of lists with the Pascal sequence.
    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    list_of_lists = []
    for i in range(1, num+1):
        list_of_lists.append([1]*i)
    for elem in range(2, len(list_of_lists)):
        for element in range(1, elem):
            list_of_lists[elem][element] = list_of_lists[elem-1][element-1] + \
            list_of_lists[elem-1][element]
    return list_of_lists

generate_pascal_triangle(5)

import doctest
print(doctest.testmod())
