def acronym(message):
    """
    get string with phrases, connected with "\n",
    give string with acronym and phrase
    >>> create_acronym("random access memory\nAs soon As possible")
    RAM - random access memory
    ASAP - As soon As possible
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
    for elem in st_ng:
        print(elem)
acronym("random access memory\nAs soon As possible")

if __name__ == "__main__":
    import doctest
    doctest.testmod()