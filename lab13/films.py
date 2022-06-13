def read_file(path: str) -> set:
    """ Return set of lines from file
    """
    general = []
    with open(path, 'r') as file:
        for line in file:
            line = line.strip('\n')
            general.append(tuple(line))
    del general[0]
            # for let in line:
            #     general.add(let)
    gen = set(general)
    return gen
print(read_file('dataa.tsv'))

def directors_dict(lines_set: set, flag) -> dict:
    """ Return dict from set of lines with film id as key
    and list of directors or writers as value
    """
    dictin = {}
    for element in lines_set:
        element = element.split()
        if flag == 'directors':
            dictin[element[0]] = dictin.get(element[0], []) + [element[1]].split(',')
        elif flag == 'writers':
            dictin[element[0]] = dictin.get(element[0], []) + [element[2]].split(',')
    print(dictin)

directors_dict(read_file('dataa.tsv'), 'directors')

def directors_max(dict_persons: dict) -> list:
    """ Return list of films with highest number of person
    """
    max_el = max(len(dict_persons[key] for key in dict_persons))
    [key for key in dict_persons if len(dict_persons[key]) == max_el]

def write_films_id(films_id) -> None:
    """ Write films id and person id to file
    """
    f = open(...)
    for line in films_id:
        f.write(line+'\n')
    f.close()

def find_directors_id(flag: str ='directors') -> None:
    """ Find films and write to files
    """
    path = ""
    line_set = read_file(path)
    dict_persons = directors_dict(line_set, 'director')
    films_id = directors_max(dict_persons)
    write_films_id(films_id)