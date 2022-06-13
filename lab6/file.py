import urllib.request
"""
Imports this module to work with txt.file
"""
def read_input_file(url, num):
    """
    Returns the txt.file with the right date.
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt', 7)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60'], ['4', 'Дмитрук А. Д.', '+', '189.123', '11.50'], ['5', 'Вінявський О. М.', '+', '189.123', '11.60'], ['6', 'Жировецька С. Г.', '+', '188.668', '11.40'], ['7', 'Чернецький В. В.', '+', '187.961', '11.20']]
    """
    line_lst = []
    with urllib.request.urlopen(url) as file:
        for line in file:
            line = line.strip()
            decoded_line = line.decode("utf-8")
            if '\t' in decoded_line:
                decoded_line = decoded_line.replace('\t', ' ')
            if 'До наказу' in decoded_line:
                line_lst.append(decoded_line.split())
            if 'Середній' in decoded_line or "Рекомендовано" in decoded_line:
                line_lst.append(decoded_line.split())
    if num > 0:
        line_lst = line_lst[:num*2]

    lst = []
    for i in range(0, len(line_lst), 2):
        line_lst[i] += line_lst[i+1]
        lst.append(line_lst[i])

    final_lst = []
    for element in lst:
        tmp = []
        tmp.append(element[0])
        tmp.append(" ".join(element[1:4]))
        tmp.append('+')
        tmp.append(element[6])
        tmp.append(element[-1])
        final_lst.append(tmp)

    return final_lst
       

a = read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt', 0)
print(a)
def write_csv_file(url):
    """
    Creates a csv.file
    """
    student_list = read_input_file(url, 0)
    with open('total.csv', 'w', encoding="utf-8") as output_file:
        first_line = "№,ПІБ,Д,Заг.бал,С.б.док.осв."
        output_file.write(first_line + "\n")
        for student in student_list:
            output_file.write(",".join(student) + "\n")

write_csv_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt')