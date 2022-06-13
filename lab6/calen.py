import calendar as cal


def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
        
    >>> weekday_name(3)
    'thu'
    """
    week_day_list = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return week_day_list[number]
    

	
def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError 
    with corresponding message
                                                
    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6                                      
    """
    date_list = date.split(".")
    for i in range(len(date_list)):
        date_list[i] = int(date_list[i])


    return cal.weekday(date_list[-1], date_list[1], date_list[0])

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
    print(calendar_string)

(calendar(8, 3003))

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
    <BLANKLINE>
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    <BLANKLINE>
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
        transformer_string.rstrip(" ")
    return transformer_string




# if __name__ == '__main__':
#     try:
#         print("Type month")
#         month = input()
#         month = int(month)
#         print("Type year")
#         year = input()
#         year = int(year)
#         print("\n\nThe calendar is: ")
#         print (calendar(month, year)) 
#     except ValueError as err:
#         print(err)
