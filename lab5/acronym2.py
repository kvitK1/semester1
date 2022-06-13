def create_acronym(message):
    """
    get string with phrases, connected with "\n",
    give string with acronym and phrase
    >>> create_acronym("random access memory")
    'RAM - random access memory'
    """
    message_list = message.split("\n")
    new_mes_list = []
    acron_list = []
    for x in message_list:
        new_mes_list.append(x.title())
    for s in new_mes_list:
        s = "".join(ch for ch in s if ch.isupper())
        acron_list.append(s)
    st_ng = []
    for i in range(0, len(acron_list)):
        st_ng.append(acron_list[i] + " - " + message_list[i])
    m = '\n'.join(st_ng)
    return m


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(create_acronym('random access memory\nAs soon As possible'))