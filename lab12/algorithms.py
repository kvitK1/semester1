''' lab_task 12_1 '''


def linear_search(list_of_values, value):
    '''
    Return index of value if value in list, else -> -1.
    >>> print(linear_search([27, 45, 89, 12, 100, -4, 36, 11], -4))
    5
    >>> print(linear_search([27, 45, 89, 12, 100, -4, 36, 11], 13))
    -1
    '''
    for i in range(len(list_of_values)):
        if list_of_values[i] == value:
            return i
    return -1


def merge_two_lists(lst1, lst2, lst):
    '''
    An additional function for def merge_sort to merge two parts of list.
    '''
    len1 = len(lst1)
    len2 = len(lst2)
    c_k = 0
    c_i = c_j = 0

    while c_i < len1 and c_j < len2:
        if lst1[c_i] < lst2[c_j]:
            lst[c_k] = lst1[c_i]
            c_i+=1
        else:
            lst[c_k] = lst2[c_j]
            c_j+=1
        c_k+=1

    while c_j < len2:
        lst[c_k] = lst2[c_j]
        c_j+=1
        c_k+=1

    while c_i < len1:
        lst[c_k] = lst1[c_i]
        c_i+=1
        c_k+=1


def merge_sort(lst):
    '''
    Return a sorted list of two merged ones.
    >>> print(merge_sort([9, 56, 82, 23, 1, 5]))
    [1, 5, 9, 23, 56, 82]
    >>> print(merge_sort([12, 356, 9, 34, 98, 45]))
    [9, 12, 34, 45, 98, 356]
    '''
    if len(lst) == 1 or len(lst) == 0:
        return lst

    middle = len(lst)//2
    left = lst[:middle]
    right = lst[middle:]
    merge_sort(left)
    merge_sort(right)
    merge_two_lists(left, right, lst)

    return lst


def binary_search(list_of_values, value):
    '''
    Return index of value if value in list, else -> -1.
    >>> print(binary_search([27, 45, 89, 12, 100, 4, 36], 36))
    3
    >>> print(binary_search([27, 45, 89, 12, 100, -4, 36], 4))
    -1
    '''
    list_of_values = sorted(list_of_values)
    high = len(list_of_values)-1
    low = 0
    while low <= high:
        middle = (low+high)//2
        if value == list_of_values[middle]:
            return middle
        elif value > list_of_values[middle]:
            low = middle+ 1
        else:
            high = middle - 1

    return -1


def selection_sort(lst):
    '''
    Return a sorted list.
    >>> print(selection_sort([23, 67, 12, 904, 56, 24]))
    [12, 23, 24, 56, 67, 904]
    '''
    for i in range(len(lst)-1):
        cur_min_inx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[cur_min_inx]:
                cur_min_inx = j
        lst[i], lst[cur_min_inx] = lst[cur_min_inx], lst[i]

    return lst


def get_pivot(lst, low, high):
    '''
    An additional function for def quick_sort to find the index of pivot.
    '''
    middle = (low+high)//2
    pivot = high
    if lst[low] < lst[middle]:
        if lst[middle] < lst[high]:
            pivot = middle
    elif lst[low] < lst[high]:
        pivot = low

    return pivot


def partition(lst, low, high):
    '''
    An additional function for def quick_sort.
    '''
    pivot_inx = get_pivot(lst, low, high)
    pivot_value = lst[pivot_inx]
    lst[pivot_inx], lst[low] = lst[low], lst[pivot_inx]
    border = low
    for i in range(low, high+1):
        if lst[i] < pivot_value:
            border+=1
            lst[i], lst[border] = lst[border], lst[i]
    lst[low], lst[border] = lst[border], lst[low]

    return border


def quick_sort_2(lst, low, high):
    '''
    An additional function for def quick_sort to work with two parts of list.
    '''
    if low < high:
        pos = partition(lst, low, high)
        quick_sort_2(lst, low, pos-1)
        quick_sort_2(lst, pos+1, high)

    return lst


def quick_sort(lst):
    '''
    Return a sorted list.
    >>> print(quick_sort([45, 67, 23, 11, 98, 24]))
    [11, 23, 24, 45, 67, 98]
    >>> print(quick_sort([45, 67, 23, 11, 98, 24, 56, 8, 34]))
    [8, 11, 23, 24, 34, 45, 56, 67, 98]
    '''
    quick_sort_2(lst, 0, len(lst)-1)
    return lst
