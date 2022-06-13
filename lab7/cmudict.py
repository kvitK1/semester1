def dict_reader_tuple(file_dict):
    """
    str -> list
    Return list with three elements.
    >>> print(dict_reader_tuple('cmudict.txt')[0:3])
    [('A', 1, ['AH0']), ('A.', 1, ['EY1']), ('A', 2, ['EY1'])]
    """

    general_list = []
    with open(file_dict, 'r', encoding='utf-8-sig') as file:
        for line in file:
            line = line.strip()
            general_list.append(line)

    new_general_list = []
    for element in general_list:
        sep_element = element.split(" ")
        new_general_list.append(sep_element)

    ready_lst = []
    for element in new_general_list:
        element[1] = int(element[1])
        list_in_tuple = list(element[2:])
        del element[2:]
        element.append(list_in_tuple)
        element = tuple(element)
        ready_lst.append(element)

    return ready_lst
dict_reader_tuple('cmudict.txt')

def dict_reader_dict(file_dict):
    """
    str -> dict
    Return dictionary with words as keys and sets of spellings as values.
    """

    general_list = []
    with open(file_dict, 'r', encoding='utf-8-sig') as file:
        for line in file:
            line = line.strip()
            general_list.append(line)  

    new_general_list = []
    for element in general_list:
        sep_element = element.split(" ")
        del sep_element[1]
        list_of_letters = tuple(sep_element[1:])
        del sep_element[1:]
        sep_element.append(list_of_letters)
        new_general_list.append(sep_element)

    ready_dict = {}
    for i in range(0, len(new_general_list)):
        set_of_values = set()
        set_of_values.add(new_general_list[i][1])
        if new_general_list[i] != new_general_list[len(new_general_list)-1]:
            if new_general_list[i][0] == new_general_list[i+1][0]:
                set_of_values.add(new_general_list[i+1][1])
        if new_general_list[i][0] not in ready_dict:
            ready_dict[new_general_list[i][0]] = set_of_values

    return ready_dict

print(dict_reader_dict('cmudict.txt'))

# import doctest
# print(doctest.testmod())

# def dict_invert(dct):
#     keys_list = list(dct.keys())
    
#     count_list = []
#     values_list = list(dct.values())
#     for elem in values_list:
#         count = len(elem)
#         if count not in count_list:
#             count_list.append(count)
#     count_list = sorted(count_list)

#     lst = []
#     for i in range(0, len(values_list)):
#         k = []
#         k.append(keys_list[i])
#         k.append(values_list[i])
#         lst.append(k)

#     print(lst)
#     print(count_list)
# dict_invert(dict_reader_dict('cmudictyk.txt'))
