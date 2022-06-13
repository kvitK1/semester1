song_titles = ['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд']
length_songs = ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21']

def lists_validation(song_titles, length_songs):
    """
    Receives elements from lists song_titles and length_songs.
    Returns if all elements are str
    """

    if len(song_titles) != len(length_songs):
        return False
    res1 = all(isinstance(element, type(song_titles[0])) for element in song_titles[1:])
    res2 = all(isinstance(element, type(length_songs[0])) for element in length_songs[1:])
    return res1 and res2

def song_length(song_info):
    """
    song_info -> tuple
    Returns the sorted list with tuples by length of second element in tuple
    """

    return song_info[1]

# song info - tuple in list
def title_length(song_info):
    """
    song_info -> tuple
    Returns the sorted list with tuples by length of first element in tuple
    """

    return len(song_info[0]) # song_info[0] - first element in tuple for sorting

def last_word(song_info):
    """
    song_info -> tuple
    Returns the sorted list with tuples by first element
    of last word in the first element
    """
    
    return song_info[0].split(" ")[-1][0].lower()
    

def sort_songs(song_titles, length_songs, key):
    """
    str, str, str -> list(tuple), function
    Returns the sorted list, according to the sorting key argument.
    >>> sort_songs(song_titles, length_songs, song_length)
    [('Етюд', '2.21'), ('Коли тебе нема', '3.17'), ('Янанебібув', '3.19'), ('Поясни', '3.39'), ('Фіалки', '3.43'), ('Відпусти', '3.52'), ('Той день', '3.58'), ('Африка', '4.24'), ('Сосни', '4.31'), ('Кавачай', '4.39'), ('Мало мені', '5.06')]
    >>> sort_songs(song_titles, length_songs, title_length)
    [('Етюд', '2.21'), ('Сосни', '4.31'), ('Африка', '4.24'), ('Поясни', '3.39'), ('Фіалки', '3.43'), ('Кавачай', '4.39'), ('Той день', '3.58'), ('Відпусти', '3.52'), ('Мало мені', '5.06'), ('Янанебібув', '3.19'), ('Коли тебе нема', '3.17')]
    >>> sort_songs(song_titles, length_songs, last_word)
    [('Африка', '4.24'), ('Відпусти', '3.52'), ('Той день', '3.58'), ('Етюд', '2.21'), ('Кавачай', '4.39'), ('Мало мені', '5.06'), ('Коли тебе нема', '3.17'), ('Поясни', '3.39'), ('Сосни', '4.31'), ('Фіалки', '3.43'), ('Янанебібув', '3.19')]
    """
    # [(str, str), (str, int), (str, int)]
    if not lists_validation(song_titles, length_songs):
        return None
    lst = []
    for i in range(len(song_titles)):
        lst.append((song_titles[i], length_songs[i]))
    lst.sort(key=key)
    return lst
sort_songs(song_titles, length_songs, song_length)

import doctest
print(doctest.testmod())

