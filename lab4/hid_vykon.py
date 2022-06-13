# import math

# def sqrt(x:float) -> float:
#     """Return square root of number ny Newton`s Method 
#     guess = 1.0 
#     new_guess = 1/2(guess + x/guess)
    
#     >>> sqrt(0.023)
#     0.15165750888103102
    
#     >>> sqrt(72)
#     8.485281374239733
#     """
    
#     def sqrt_iter():
#         guess = 1.0
#         while not good_enough(guess):
#             guess = improve(guess)
#             print(guess)
#         return guess
   

#     def improve(guess):
#         return average(guess, x/guess)
  
#     def average(x, y):
#         return (x+y)/2
   

#     def good_enough(guess):
#         number = guess
#         if math.isclose(number**2, x):
#             return 1
#         else:
#             return 0
    
#     return print(f"square root of {x} = {sqrt_iter()}")
# sqrt(72)

# def type_by_sides(a, b, c):
#     if a+b < c or a+c < b or c+b < a:
#         return None
#     else:
#         if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#             print('right angled triangle')
#         elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
#             print('obutuse triangle')
#         elif a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or b**2 + c**2 > a**2:
#             print('acute triangle')
# type_by_sides(12, 13, 5)

# def remove_spaces(s):
#     """
#     str -> str
#     Remove all additional spaces in string and return a new string without additional spaces.
#     If argument is not a string function should return None.

#     >>> remove_spaces("I'll make     him an     offer he can't refuse.")
#     I'll make him an offer he can't refuse.
#     >>> remove_spaces("Great    men     are    not born great, they grow great...")
#     Great men are not born great, they grow great...
#     >>> remove_spaces(2015)

#     """
#     if type(s) != str:
#         return None

#     string1 = ""
#     for i in range(0, len(s)):
#         if i>0 and s[i] == s[i-1] == " ":
#             continue
#         string1 += s[i]
#     print(string1)
# remove_spaces()


# ****************************************
# Problem 9
# ****************************************
# def replace_with_stars(s):
#     """
#     str -> str
#     Replace symbols in string with stars. If argument is not a string function should
#     return None.

#     >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
#     ****************************************************
#     >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
#     **************************************************
#     >>> number_of_sentences(2015)

#     """
#     if type(s) != str:
#         return None

#     string = s.replace(s, "*"*len(s))
#     print(string)
# replace_with_stars()


# ****************************************
# Problem 10
# ****************************************
# def encrypt_message(s):
#     """
#     str -> str
#     Replace all letters in string with next letters in aplhabet. If argument is not a string
#     function should return None.

#     >>> encrypt_message("Revenge is a dish that tastes best when served cold.")
#     Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.
#     >>> encrypt_message("Never hate your enemies. It affects your judgment.")
#     Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.
#     >>> encrypt_message(2015)

#     """
#     string = ""
#     if type(s) != str:
#         return None 
#     for i in s:
#         if i == " " or i == ".":
#             string += i
#             continue
#         string += chr(ord(i)+1)
#     print(string)

# encrypt_message("Never hate your enemies. It affects your judgment.")   

# ****************************************
# Problem 11
# ****************************************
# def decrypt_message(s):
#     """
#     str -> str
#     Replace all letters in string with previous letters in aplhabet. If argument isn't a string
#     function should return None.

#     >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
#     Revenge is a dish that tastes best when served cold.
#     >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
#     Never hate your enemies. It affects your judgment.
#     >>> decrypt_message(2015)

#     """ 
#     string = ""
#     if type(s) != str:
#         return None

#     for i in s:
#         if i == " " or i == ".":
#             string += i
#             continue
#         string += chr(ord(i)-1)
#     print(string)
# decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")


# ****************************************
# Problem 13
# ****************************************
# def create_string(lst):
#     import string
#     """
#     list -> str
#     Create and return string from histogrma of letters. If argument isn't list of 26 positive
#     integer numbers function should return None.

#     >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     bcc
#     >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4])
#     aaaazzzz
#     >>> create_string([4, 0, 0, 0, 0, 0])

#     """
#     new_string = ""
#     alpha_list = list(string.ascii_lowercase)
#     if len(lst) < 26:
#         return None

#     for i in range(0, len(lst)):
#         if lst[i] < 0:
#             return
#         new_string += alpha_list[i]*lst[i]
#     print(new_string)
# create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4])

# ****************************************
# Problem 18
# ****************************************
# def number_of_capital_letters(s):
#     import string
#     """
#     str -> str
#     Find and return number of capital letters in string. If argument isn't string
#     function should return None.

#     >>> number_of_capital_letters("ArithmeticError")
#     2
#     >>> number_of_capital_letters("EOFError")
#     4
#     >>> number_of_capital_letters(1)

#     """
#     new_string = []
#     alpha_upper = list(string.ascii_uppercase)
#     if type(s) != str:
#         return None 
    
#     for i in range(0, len(s)):
#         if s[i] not in alpha_upper:
#             continue
#         new_string += s[i]
#     print(len(new_string))
# number_of_capital_letters("ArithmetiCError")

# ****************************************
# Problem 20
# ****************************************
# def polynomial_eval(coefficients, value):
#     """
#     # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
#     >>> polynomial_eval([2,3,0,4], 4)
#     180
#     # f(x) = 6, f(42) = 6
#     >>> polynomial_eval([6], 42)
#     6
#     # f(x) = 6x^2 -2x - 20, f(-1) = -12
#     >>> polynomial_eval([6,-2,-20], -1)
#     -12
#     # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
#     >>> polynomial_eval([6,0,-8,0,-8,0], 2)
#     112
#     >>> polynomial_eval([6,0,-8,0,-8,0], 1)
#     -10
#     >>> polynomial_eval([6,0,-8,0,-8,0], 0)
#     0
#     """
#     string = []
#     sum = 0
#     step = len(coefficients)-1
#     for i in range(0, len(coefficients)):
#         string.append(coefficients[i] * (value**step))
#         step -= 1
#     for j in range(0, len(string)):
#         sum += string[j]
#     print(sum)
# polynomial_eval([6,0,-8,0,-8,0], 0)


# ****************************************
# Problem 21
# ****************************************
def polynomials_multiply(polynom1, polynom2):
    """
    # (2x)*(3x) == 6
    >>> polynomials_multiply([2], [3])
    [6]
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    >>> polynomials_multiply([2,-4],[3,5])
    [6,-2,-20]
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    >>> polynomials_multiply([2,0,-4],[3,0,2,0])
    [6,0,-8,0,-8,0]

    """
    
# def nice_hello():
#     s = 'Hello, World!'
#     new_s = ''
#     for i in range(len(s)):
#         new_s += s[i] + '\n'
    
#     return new_s            

# nice_hello()

# def f():
#     print(2 ** 2)
#     return 2 ** 3
# f()

# def f(a):
#     a = 1
#     return a ** 2
# f(2)
# def nice_hello():
#     s = 'Hello, World!'
#     new_s = ''
#     for c in range(len(s)):
#         new_s = i + new_s
    
#     return new_list

# nice_hello()

a = 1

def f():
    if 'a' in dir():     
        print(a)
    else:
        print(10)
f()

def change(x):
    x = (2016, 2016)

x = (2015, 2016)
change(x)
print(x)

def is_positive(x):
    print("False!")   
    return x > 0
    print("True!")

is_positive(3)


def change(s):
    s = 'Hello, ' + s

s = 'Andrew'
change(s)
print(s)

def change(lst):
    lst.append(2016)

lst = [2014, 2015]
change(lst)
print(lst)

def change(x):
    x += 1

x = 2016
change(x)
print(x)