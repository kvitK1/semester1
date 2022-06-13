# ****************************************
# Problem 5
# ****************************************
# def type_by_sides(a, b, c):
#     """
#     (float, float, float) -> str
#     Detect the type of triangle by it's sides and return type as string
#     ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
#     triangle with such sides, then function should return None.
    
#     acute triangle = гострокутний
#     obutuse triangle = тупокутний

#     >>> type_by_sides(3, 3, 3)
#     "acute triangle"
#     >>> type_by_sides(3, 4, 5)
#     "right angled triangle"
#     >>> type_by_sides(3, 3, 2015)
#     """
#     if a+b < c or a+c < b or c+b < a:
#         return None
#     else:
#         if a+b < c or a+c < b or c+b < a:
#             return None
#         else:
#             if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#                 print('right angled triangle')
#             elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
#                 print('obutuse triangle')
#             elif a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or b**2 + c**2 > a**2:
#                 print('acute triangle')
# type_by_sides(4, 3, 5)

# def convert_to_column(s):
#     """
#     str -> str
#     Convert string to a column of words.
#     If argument is not a string function should return None.

#     >>> print_column("Revenge is a dish that tastes best when served cold.")
#     revenge
#     is
#     a
#     dish
#     that
#     tastes
#     best
#     when
#     served
#     cold
#     >>> print_column("Never hate your enemies. It affects your judgment.")
#     never
#     hate
#     your
#     enemies
#     it
#     affects
#     your
#     judgment
#     >>> print_column(2015)
#     """
#     string = ""
#     if type(s) != str:
#         return None

#     for i in range(0, len(s)):
#         if i>0 and s[i] == ".":
#             continue
#         string += s[i].lower()
#     new_string = string.split()
        
#     print(*new_string, sep="\n")

# convert_to_column("Revenge is a dish that tastes best when served cold.")

# def convert_to_column(s):
#     """
#     str -> str
#     Convert string to a column of words.
#     If argument is not a string function should return None.

#     >>> print_column("Revenge is a dish that tastes best when served cold.")
#     revenge
#     is
#     a
#     dish
#     that
#     tastes
#     best
#     when
#     served
#     cold
#     >>> print_column("Never hate your enemies. It affects your judgment.")
#     never
#     hate
#     your
#     enemies
#     it
#     affects
#     your
#     judgment
#     >>> print_column(2015)
#     """
#     if type(s) != str:
#         return None

#     print(*s.replace(".", "").lower().split(), sep="\n")
# convert_to_column("Revenge is a dish that tastes best when served cold.")

   # ****************************************
# Problem 22
# ****************************************
def pattern_number(sequence):
    """
    >>> pattern_number([])
    None
    >>> pattern_number([42])
    None
    >>> pattern_number([1,2])
    None
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    None
    >>> pattern_number([1,2,3,1,2,3])
    ([1,2,3], 2)
    >>> pattern_number([1,2,3,1,2])
    None
    >>> pattern_number([1,2,3,1,2,3,1])
    None
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    None
    """
    