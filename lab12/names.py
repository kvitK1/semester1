""" lab 12_2 """


def read_file(path):
    """
    Return a list of lists with name and number.
    >>> print(len(read_file('boy_names.txt')))
    319
    """
    general_list = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split()
            general_list.append(line)
    general_list.remove(general_list[0])
    for _, val in enumerate(general_list):
        val[1] = int(val[1].replace('(', '').replace(')', ''))

    return general_list


def selection_sort(lst):
    """
    Return a sorted list.
    >>> print(selection_sort([23, 67, 12, 904, 56, 24]))
    [12, 23, 24, 56, 67, 904]
    """
    for i in range(len(lst)-1):
        cur_min_inx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[cur_min_inx]:
                cur_min_inx = j
        lst[i], lst[cur_min_inx] = lst[cur_min_inx], lst[i]

    return lst


def find_3(names_list):
    """
    Return a set with three most popular names.
    >>> print(len(find_3(read_file('boy_names.txt'))))
    3
    """
    number_list = []
    for elem in names_list:
        number_list.append(elem[1])
    selection_sort(number_list)
    names_3_set = set()

    for element in names_list:
        if element[1] == number_list[-1] or element[1] == number_list[-2] or \
        element[1] == number_list[-3]:
            names_3_set.add(element[0])

    return names_3_set


def only_once(names_list):
    """
    Return a tuple: num of names and list of names, which were used only once.
    >>> print(len(only_once(read_file('boy_names.txt'))))
    2
    """
    once_name = set()
    for element in names_list:
        if element[1] == 1:
            once_name.add(element[0])

    return (len(once_name), once_name)


def find_letter(names_list):
    """
    Return a tuple with: a letter, num of names, num of children.
    >>> print(find_letter(read_file('boy_names.txt')))
    ('А', 41, 1065)
    >>> print(find_letter(read_file('girl_names.txt')))
    ('А', 55, 1752)
    """
    let_set = set()
    for element in names_list:
        let_set.add(element[0][0])

    list_w_names = []
    for item in let_set:
        lst = []
        for elem in names_list:
            if elem[0][0] == item:
                lst.append(elem[0])
        list_w_names.append(lst)

    names_dict = {}
    for elemnt in list_w_names:
        names_dict[elemnt[0][0]] = (len(elemnt), elemnt)
    max_num = max(names_dict.values())

    counter = 0
    for name in max_num[1]:
        for elm in names_list:
            if elm[0] == name:
                counter += elm[1]

    return (max_num[1][0][0],len(max_num[1]), counter)


def find_names(file_path):
    """
    Return a tuple with datas from the additional functions.
    >>> print(len(find_names('boy_names.txt')))
    3
    >>> print(len(find_names('girl_names.txt')))
    3
    """
    el1 = find_3(read_file(file_path))
    el2 = only_once(read_file(file_path))
    el3 = find_letter(read_file(file_path))
    return (el1, el2, el3)
print(find_names('/Users/kvitoslava/vscode_intro/lab12/girl_names.txt'))