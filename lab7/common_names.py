def names_read(file_name):
    """
    str -> list
    Return list with names.
    >>> print(names_read("female.txt")[0])
    Abagael
    """
    general_list = []
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        for line in file:
            line = line.strip()
            general_list.append(line)

    return general_list


def common_names(female_names, male_names):
    """
    (list, list) -> set
    Return a set with names, which've been in both lists and start with vowel.
    >>> print(len(common_names(names_read("female.txt"), names_read("male.txt"))))
    40
    """
    female_set = set(female_names)
    male_set = set(male_names)
    common_set = female_set.intersection(male_set)

    vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    set_common_names = set()
    for name in common_set:
        if name[0] in vowels_list:
            set_common_names.add(name)

    return set_common_names

# common_names(names_read("female.txt"), names_read("male.txt"))

import doctest
print(doctest.testmod())