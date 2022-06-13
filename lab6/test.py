# def summ(string):
#     """
#     string -> str
#     Returns the sum of all characters in string
    
#     """
#     summa = 0
# #     for i in string:
# #         summa += int(i)
# #     return summa

# # def happy_number(num):
# #     """
# #     num -> int
# #     Returns True or False if the left side is equal to right side of the number
# #     >>> happy_number(12345)
# #     False
# #     >>> happy_number(43211234)
# #     True
# #     >>> happy_number(191234)
# #     True
# #     """

# #     string = str(num)
# #     new_string = ""
# #     if len(string) < 8:
# #         new_string = '0'*(8-len(string)) + string
# #     return summ(new_string[:4]) == summ(new_string[4:])

# # def happy_numbers(m, n):
# #     """
# #     m, n -> int
# #     Returns the list filled with all possible lucky numbers between m and n
# #     """
# #     lst = []
# #     for i in range(m, n+1):
# #         if happy_number(i) == True:
# #             lst.append(i)
# #     return lst

# # def count_happy_numbers(n):
# #     happy_lst = 0
# # #     for i in range(1, n+1):
# # #         if happy_number(i) == True:
# # #             happy_lst += 1
# # #     return print(happy_lst)
# # # count_happy_numbers(58990)

# # # for i in zip(song[0], song[1], song[2]): print(i)
# # # ('чотири', 'роки', 'були') ('сім', 'днів', 'на тиждень') ('двадцять', 'нас', 'разом')
# # # >>> for i in zip(*song): print(i)
# # # ('чотири', 'роки', 'були') ('сім', 'днів', 'на тиждень') ('двадцять', 'нас', 'разом')

# # # def summ(string):
# # #     """
# # #     string -> str
# # #     Returns the sum of all characters in string
# # #     """

# # #     summa = 0
# # #     for i in string:
# # #         summa += int(i)
# # #     return summa

# # # def happy_number(num):
# # #     """
# # #     num -> int
# # #     Returns True or False if the left side is equal to right side of the number
# # #     >>> happy_number(12345)
# # #     False
# # #     >>> happy_number(43211234)
# # #     True
# # #     >>> happy_number(191234)
# # #     True
# # #     """

# # #     string = str(num)
# # #     new_string = ""
# # #     if len(string) < 8:
# # #         new_string = '0'*(8-len(string)) + string
# # #     return summ(new_string[:4]) == summ(new_string[4:])

# # # def happy_numbers(m, n):
# # #     """
# # #     m, n -> int
# # #     Returns the list filled with all possible lucky numbers between m and n
# # #     >>> happy_numbers(245, 260)
# # #     [245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260]
# # #     """
# # #     lst = []
# # #     for i in range(m, n+1):
# # #         if happy_number(i) == True:
# # #             lst.append(i)
# # #     return lst
# # # happy_numbers(245, 260)

# # import calendar as cal
# # # def weekday(date: str) -> int:
# # #     """
# # #     Return an integer representing a weekday
# # #     (0 represents monday and so on)
# # #     Read about algorithm as Zeller's Congruence
# # # #     date : a string of form "day.month.year
# # # #     if the date is invalid raises AssertionError 
# # # #     with corresponding message
                                                
# # # #     >>> weekday("12.08.2015")
# # # #     2
# # # #     >>> weekday("28.02.2016")
# # # #     6                                      
# # # #     """
# # # #     date_list = date.split(".")
# # # #     for i in range(len(date_list)):
# # # #         date_list[i] = int(date_list[i])
# # # #     week = cal.weekday(date_list[2], date_list[1], date_list[0])
# # # #     return week
# # # # weekday("28.10.2020")



# # def calendar(month: int, year: int) -> str:
# #     """Return a string representing a\
# #     horizontal calendar for the given month and year.

# #     month : an integer in range [1 , 12]
# #     year : an integer (strictly speaking the algorithm in weekday
# #            works correctly only for Gregorian calendar, so year must
# #            be greater than 1583)
# #     when arguments are invalid raises AssertionError with corresponding
# #     message

# #     >>> print(calendar(8 , 2015))
# #     mon tue wed thu fri sat sun
# #                           1   2
# #       3   4   5   6   7   8   9
# #      10  11  12  13  14  15  16
# #      17  18  19  20  21  22  23
# #      24  25  26  27  28  29  30
# #      31
# #     """

# #     if month not in range(1, 13):
# #         raise AssertionError("not valid month")

# #     if year <= 1583:
# #         raise AssertionError("not valid year")

# #     calendar_list = cal.monthcalendar(year, month)
# #     header = cal.weekheader(month).lower()
# #     header = header.split()
# #     header = " ".join(header)
# #     calendar_string = ""

# #     for element in calendar_list:
# #         string_l = [str(i) for i in element]

# #         for d in range(len(string_l)):
# #             if string_l[d] == "0":
# #                 string_l[d] = " "

# #             if len(string_l[d]) < 2:
# #                 string_l[d] = "  " + string_l[d]
# #             else:
# #                 string_l[d] = " " + string_l[d]
# #         new_string = " ".join(string_l)
# #         calendar_string += new_string + "\n"
# #     calendar_string = header + "\n" + calendar_string
# #     calendar_string = calendar_string[:-1]
# #     return calendar_string
# # calendar(8 , 2015)

# # def transform_calendar(calendar: str) -> str:
# #     """Return a modified horizontal -> vertical calendar.

# #     calendar is a string of a calendar, returned by the calendar()
# #     function.
# #     >>> print(transform_calendar(calendar(5, 2002)))
# #     mon   6 13 20 27
# #     tue   7 14 21 28
# #     wed 1 8 15 22 29
# #     thu 2 9 16 23 30
# #     fri 3 10 17 24 31
# #     sat 4 11 18 25
# #     sun 5 12 19 26
# #     >>> print(transform_calendar(calendar(8 , 2015)))
# #     mon   3 10 17 24 31
# #     tue   4 11 18 25
# #     wed   5 12 19 26
# #     thu   6 13 20 27
# #     fri   7 14 21 28
# #     sat 1 8 15 22 29
# #     sun 2 9 16 23 30
# #     """

# #     calendar_list = calendar.split("\n")
# #     for k in range(len(calendar_list)):
# #         if len(calendar_list[k]) == 0:
# #             del calendar_list[k]

# #     for i in range(len(calendar_list)):
# #         calendar_list[i] = calendar_list[i].split()
# #         if i == 1:
# #             num = 7 - len(calendar_list[i])
# #             tmp = []
# #             j = 0
# #             while j < num:
# #                 tmp.append(" ")
# #                 j += 1
# #             calendar_list[i] = tmp + calendar_list[i]
# #         if i == len(calendar_list)-1:
# #             num = 7 - len(calendar_list[i])
# #             tmp = []
# #             j = 0
# #             while j < num:
# #                 tmp.append(" ")
# #                 j += 1
# #             calendar_list[i] = calendar_list[i] + tmp
    
# #     transformed_calendar = []
# #     transformer_string = ""
# #     for i in range(7):
# #         tmp = []
# #         for element in calendar_list:
# #             tmp.append(element[i])
# #         transformed_calendar.append(tmp)
# #     for elem in transformed_calendar:
# #         transformer_string += " ".join(elem) + "\n"
# #     transformer_string = transformer_string[:-1]
# #     a = transformer_string[::-1]
# #     for i in a:
# #         if i != " ":
# #             inx = a.index(i)
# #             break
# #     a = a[inx:]
# #     transformer_string = a[::-1]

# #     return transformer_string
# # transform_calendar(calendar(5, 2002))

    

# def summ(string):
#     """
#     str -> int
#     Returns the sum of all characters in string.
#     """

#     summa = 0
#     for i in string:
#         summa += int(i)
#     return summa

# def happy_number(num):
#     """
#     int -> bool
#     Returns True or False if the left side is equal to right side of the number.
#     >>> print(happy_number(12345))
#     False
#     >>> print(happy_number(43211234))
#     True
#     >>> print(happy_number(191234))
#     True
#     """

#     string = str(num)
#     new_string = ""
#     if len(string) < 8:
#         new_string = '0'*(8-len(string)) + string
#     return summ(new_string[:4]) == summ(new_string[4:])

# def happy_numbers(num1: int, num2: int):
#     """
#     Returns the list filled with all possible lucky numbers between m and n.
#     >>> print(happy_numbers(245, 260))
#     []
#     """
#     lst = []
#     for i in range(num1, num2+1):
#         if happy_number(i) == True:
#             lst.append(i)
#     return lst

# def count_happy_numbers(num):
#     """
#     int -> int
#     Returns the number of lucky numbers.
#     >>> count_happy_numbers(58990)
#     125
#     """

#     happy_lst = 0
#     for i in range(1, num+1):
#         if happy_number(i) == True:
#             happy_lst += 1
#     return print(happy_lst)

import calendar as cal
def calendar(month: int, year: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """

    if month not in range(1, 13):
        raise AssertionError("not valid month")

    if year <= 1583:
        raise AssertionError("not valid year")

    calendar_list = cal.monthcalendar(year, month)
    header = cal.weekheader(month).lower()
    header = header.split()
    header = " ".join(header)
    calendar_string = ""

    for element in calendar_list:
        string_l = [str(i) for i in element]

        for d in range(len(string_l)):
            if string_l[d] == "0":
                string_l[d] = " "

            if len(string_l[d]) < 2:
                string_l[d] = "  " + string_l[d]
            else:
                string_l[d] = " " + string_l[d]
        new_string = " ".join(string_l)
        calendar_string += new_string + "\n"
    calendar_string = header + "\n" + calendar_string
    return calendar_string
calendar(8 , 2015)


def transform_calendar(calendar: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """

    calendar_list = calendar.split("\n")
    for k in range(len(calendar_list)):
        if len(calendar_list[k]) == 0:
            del calendar_list[k]

    for i in range(len(calendar_list)):
        calendar_list[i] = calendar_list[i].split()
        if i == 1:
            num = 7 - len(calendar_list[i])
            tmp = []
            j = 0
            while j < num:
                tmp.append(" ")
                j += 1
            calendar_list[i] = tmp + calendar_list[i]
        if i == len(calendar_list)-1:
            num = 7 - len(calendar_list[i])
            tmp = []
            j = 0
            while j < num:
                tmp.append(" ")
                j += 1
            calendar_list[i] = calendar_list[i] + tmp
    
    transformed_calendar = []
    transformer_string = ""
    for i in range(7):
        tmp = []
        for element in calendar_list:
            tmp.append(element[i])
        transformed_calendar.append(tmp)
    for elem in transformed_calendar:
        transformer_string += " ".join(elem) + "\n"
    transformer_string = transformer_string[:-1]
    return print(transformer_string)
(transform_calendar(calendar(8 , 2015)))


# import doctest
# print(doctest.testmod())

