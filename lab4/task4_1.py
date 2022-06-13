def dyvo_insert(sentence, flag):
    """
    Add "диво" before every element in sentence, which starts with flag
    >>> dyvo_insert('Кит кота по хвилях катав - кит у воді, кіт на киті', "ки")
    'дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    >>> dyvo_insert('Кит кита по хвилях катав - кит у воді, кит на киті', "ки")
    'дивокит дивокита по хвилях катав - дивокит у воді, дивокит на дивокиті'
    >>> dyvo_insert('Кит кита по хвилях катав - кит у воді, кит на киті', "ик")
    'кит кита по хвилях катав - кит у воді, кит на киті'
    """
    sentence = sentence.lower().split(" ")
    sent = ""
    for i in sentence:
        if i.startswith(flag):
            i = "диво" + i
        sent += i + " "
    print(sent[:-1])

dyvo_insert('Кит кота по хвилях катав - кит у воді, кіт на киті', "ки")