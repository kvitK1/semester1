history_list = [('https://www.google.com/search?q=w3school&oq=w3school&aqs=chrome..0j69i57j0l6.4077j0j7&sourceid=chrome&ie=UTF-8', 'w3school - Пошук Google', '2020-10-16', '13:24:16.177378', 0),
('https://www.w3schools.com/', 'W3Schools Online Web Tutorials', '2020-10-11', '13:24:20.047577', 11263539),
('https://www.w3schools.com/sql/default.asp', 'SQL Tutorial', '2020-10-17', '13:24:31.311115', 17416891),
('https://www.w3schools.com/sql/sql_insert.asp', 'SQL INSERT INTO Statement', '2020-10-17', '13:24:48.728006', 240341066),
('https://www.w3schools.com/sql/trysql.asp?filename=trysql_insert_colname', 'SQL Tryit Editor v1.6', '2020-10-17', '13:25:01.342619', 227568961),
('file:///Users/liubchyk/Desktop/LiubomyrOleksiuk2.html', 'Табличка', '2020-10-17', '13:28:59.622938', 78858673),
('file:///Users/liubchyk/Desktop/LiubomyrOleksiuk2.html', 'Табличка', '2020-10-16', '17:26:59.622938', 788586),
('file:///Users/liubchyk/Desktop/LiubomyrOleksiuk1.html', 'My CV', '2020-10-18', '10:53:30.550131', 169148385),
('file:///Users/liubchyk/Desktop/LiubomyrOleksiuk2.html', 'Табличка', '2020-10-12', '13:28:59.622938', 78858673),
('file:///Users/liubchyk/Desktop/LiubomyrOleksiuk2.html', 'Табличка', '2020-10-18', '10:56:10.623882', 6305992793),
('file:///Users/liubchyk/Desktop/LiubomyrOleksiuk1.html', 'My CV', '2020-10-18', '10:56:37.332443', 7714798),
('file:///Users/liubchyk/Desktop/LiubomyrOleksiuk1.html', 'My CV', '2020-10-10', '10:56:37.332443', 7714798),
('file:///Users/liubchyk/Desktop/LiubomyrOleksiuk3.html', 'Анкета', '2020-10-18', '11:00:32.339073', 0),
('file:///Users/liubchyk/Desktop/LiubomyrOleksiuk3.html', 'Анкета', '2020-10-18', '11:00:59.716379', 6016898150),
('file:///Users/liubchyk/Desktop/erge.html', 'fb', '2020-10-18', '11:46:58.846092', 0)]

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

print(sites_on_date([('https://', 'googl', '2020-10-11', '13:24:16.177378', 11)], '2020-10-11'))

print(sites_on_date([('https://', 'googl', '2020-10-11', '13:24:16.177378', 11)], '2020-10-11'))
from collections import Counter 
def most_frequent_sites(visits: list, number: int):
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> print(most_frequent_sites([('gog', 'anket'), ('gog', 'an'), ('le', 'ke'), ('gog', 'ke')], 1))
    {'gog'}
    """
    lst = []
    for tuple_site in visits:
        lst.append(tuple_site[0])
    c_func = Counter(lst)
    frequent_list = c_func.most_common(number)
    ready_set = set()
    for element in frequent_list:
        ready_set.add(element[0])
    
    return ready_set

print(most_frequent_sites([('gog', 'anket'), ('gog', 'an'), ('le', 'ke'), ('gog', 'ke')], 1))

def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    >>> print(get_url_info([('https://', 'googl', '2020-10-11', '13:24:16.177378', 11)], 'https://'))
    ('googl', '2020-10-11', '13:24:16.177378', 11)
    """
    lst = []
    for i in range(0, len(visits)):
        if url == visits[i][0]:
            lst.append(visits[i])
    num_attendance = len(lst)
    count = 0
    new_lst = []
    for element in lst:
        count += element[4] 
    ready_count = count/num_attendance
    for elem in range(0, len(lst)):
        while elem != len(lst)-1:
            continue
        else:
            inx = len(lst) - 1
            new_lst.append(lst[inx])
            ready_set = (new_lst[inx][0], new_lst[inx][1], new_lst[inx][2], new_lst[inx][3], ready_count)
    print(ready_set)

get_url_info([('https:', 'googl', '2020-10-10', '13:24:16.177378', 11), ('https:', 'googllll', '2020-10-11', '14:24:16.177378', 17)], 'https:')

# import doctest
# print(doctest.testmod())