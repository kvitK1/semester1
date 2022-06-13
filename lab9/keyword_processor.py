# from  films_keywords_v1 import input_from_file
# print(input_from_file())
keys_test = {'friend': ['"#1 Single"', '"10 Play"', '"#ATown"']}
    # 'web-series': ['"#1MinuteNightmare" (2014)', '"#30Nods" (2016)', '"#1 Single" (2006)'], 
    # 'friend': ['"#30Nods" (2016)', '"\'Allo \'Allo!" (1982)', '"#1 Single" (2006)'],
    # 'heroin': ['"#30Nods" (2016)', '"#1MinuteNightmare" (2014)'], 
    # 'vlog': ['"#30Nods" (2016)', '"#1 Single" (2006)', '"10 Play" (2002)'], 
    # 'austin-texas': ['"#ATown" (2014)', '"#1MinuteNightmare" (2014)'], 
    # 'beer': ['"#ATown" (2014)', '"\'Allo \'Allo!" (1982)', '"#1 Single" (2006)'],
    # 'drugs': ['"#ATown" (2014)', '"#30Nods" (2016)', '"10 Play" (2002)'], 
    # 'friendship': ['"#ATown" (2014)', '"\'Allo \'Allo!" (1982)', '"#30Nods" (2016)']

"""keyword_processor, task9_1"""

def find_film_keywords(film_keywords: dict, film_name: str):
    """
    Return set with keywords, which might be faced in the film.
    >>> print(find_film_keywords({'friend': ['"Single"', '"Play"', '"ATown"']}, '"ATown"'))
    {'friend'}
    >>> print(find_film_keywords({'friend': ['"Single"', '"Play"', '"ATown"']}, '"a_Town"'))
    set()
    """

    return {keyword for keyword in film_keywords if film_name in film_keywords[keyword]}


def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    """
    Return a list of tuples with the film name and number of keywords it has.
    >>> print(len(find_films_with_keywords({'friend': ['"#1 Single"', '"10 Play"', '"#ATown"']}, 2)))
    2
    >>> print(find_films_with_keywords({'friend': ['"#1 Single"', '"10 Play"', '"#ATown"']}, 0))
    []
    """
    list_of_films = list()
    set_of_films = set()
    for keyword in film_keywords:
        for film in film_keywords[keyword]:
            set_of_films.add(film)
    for film_name in set_of_films:
        counter = 0
        for keyword in film_keywords:
            if film_name in film_keywords[keyword]:
                counter += 1
        list_of_films.append((film_name, counter))
    full_list = sorted(list_of_films, key=lambda x: x[1], reverse=True)

    return full_list[:num_of_films]


# print(find_film_keywords({'friend': ['"Single"', '"Play"', '"ATown"']}, '"Town"'))
# print(find_films_with_keywords(keys_test, 0))

import doctest 
print(doctest.testmod())
