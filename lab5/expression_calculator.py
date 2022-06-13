def calculate_expression(expression):
    """
    str -> int, str
    Returns the result. 
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    express = str(expression).split()
    if express[-1][-1] == "?":
        last_elem = express[-1][:-1]
        express[-1] = last_elem
    express.pop(0)
    express.pop(0)
    lst = []
    for j in express:
        if j  == "на":
            express.remove(j)
        # if j != "додати" or j != "відняти" or j != "помножити" or j != "поділити":
        #     print('Неправильний вираз!')
    
    for i in range(len(express)):
        if express[i] == "додати" or express[i] == "плюс":
            express[i] = "+"
        elif express[i] == "відняти" or express[i] == "мінус":
            express[i] = "-"
        elif express[i] == "помножити":
            express[i] = "*"
        elif express[i] == "поділити":
            express[i] = "/"
    m = "".join(express)
    print(m)
    print(int(eval(m)))

calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()