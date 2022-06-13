def caesar_encode(message, key):
    """
    ceasar_encode function
    >>> caesar_encode("this is my computer", 3)
    wklv lv pb frpsxwhu
    """
    new_string = ""
    for elemn in message:
        if elemn == " ":
            new_string += elemn
        else:
            elem = ord(elemn) + key
            while elem > ord("z"):
                elem -= 26
            new_elem = chr(elem)
            new_string += new_elem

    print(new_string)
caesar_encode("apple juice", 40)

def caesar_decode(message, key):
    """
    ceasar_decode function
    >>> caesar_decode("wklv lv pb frpsxwhu", 3)
    this is my computer
    """
    new_string = ""
    for elemn in message:
        if elemn == " ":
            new_string += elemn
        else:
            elem = ord(elemn) - key
            while elem < ord("a"):
                elem += 26
            new_elem = chr(elem)
            new_string += new_elem

    print(new_string)
caesar_decode("oddzs xiwqs", 40)

if __name__ == "__main__":
    import doctest
    doctest.testmod()