import sys

def return_digits(number):
    r"""
    int or str -> str
    Returns a picture of numbers.
    >>> return_digits(787)
    '77777 888 77777\n    78   8    7\n   7 8   8   7 \n  7   888   7  \n 7   8   8 7   \n7    8   87    \n7     888 7    \n'
    >>> return_digits(12)
    ' 1  222 \n11 2   2\n 1 2  2 \n 1   2  \n 1  2   \n 1 2    \n11122222\n'
    """
    digits = str(number)
    alibaba = ""
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row].replace("*", str(number))
            column += 1
        alibaba += line + "\n"
        row += 1
    return print(alibaba)

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row].replace("*", str(number))
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bidigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
return_digits(65)

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()