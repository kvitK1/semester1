''' a module with recursive functions to work with lists.'''


def flatten(lst):
    """
    Returns a flattenned list or an object if it is not a list.
    >>> print(flatten([1,2,[3,[4,5],6],7]))
    [1, 2, 3, 4, 5, 6, 7]
    >>> print(flatten([[]]))
    []
    >>> print(flatten(['wow', [2,[[]]], [True]]))
    ['wow', 2, True]
    >>> print(flatten(3))
    3
    """

    if not isinstance(lst, list):
        return lst
    if len(lst) == 0:
        return lst
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return lst[:1] + flatten(lst[1:])


def create_table(rows, columns):
    """
    Returns a list of list with number sequences.
    >>> print(create_table(2, 6))
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6]]
    >>> print(create_table(5, 3))
    [[1, 1, 1], [1, 2, 3], [1, 3, 6], [1, 4, 10], [1, 5, 15]]
    >>> print(create_table(1, 8))
    [[1, 1, 1, 1, 1, 1, 1, 1]]
    >>> print(create_table(0, 8))
    Please, enter a natural number, etc. more than 0!
    """

    if rows <= 0:
        return "Please, enter a natural number, etc. more than 0!"
    elif rows == 1:
        print(f'prev_row={[[1]*columns]}')
        return [[1]*columns]
    else:
        prev_row = create_table(rows-1, columns)
        print(f'prev_row={prev_row}')
        next_row = [1]*columns
        for inx in range(1, columns):
            next_row[inx] = next_row[inx-1] + prev_row[rows-2][inx]
        return prev_row + [next_row]

print(create_table(4, 6))