def sites_on_date(visits: list, date: str):
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    >>> print(sites_on_date([('https://', 'googl', '2020-10-11', '13:24:16.177378', 11)], '2020-10-11'))
    {'https://'}
    """
    lst = []
    set_common = set()
    for tuple_site in visits:
        tuplyk = (tuple_site[0], tuple_site[2])
        lst.append(tuplyk)
    for i in range(0, len(lst)):
        if lst[i][1] == date:
            set_common.add(lst[i][0])

    return set_common