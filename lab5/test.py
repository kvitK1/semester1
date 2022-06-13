# def calculate_expression(expression):
#     """
#     it calculates the expression
#     >>> calculate_expression("Скільки буде 8 відняти 3?")
#     5
#     >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
#     50
#     >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
#     9
#     >>> calculate_expression("Скільки буде 3 в кубі?")
#     'Неправильний вираз!'
#     """
#     express = str(expression).split()
#     if express[-1][-1] == "?":
#         last_elem = express[-1][:-1]
#         express[-1] = last_elem
#     express.pop(0)
#     express.pop(0)
#     lst = []
#     for j in express:
#         if j  == "на":
#             express.remove(j)
#         # if j != "додати" or j != "відняти" or j != "помножити" or j != "поділити":
#         #     print('Неправильний вираз!')
    
#     for i in range(len(express)):
#         if express[i] == "додати" or express[i] == "плюс":
#             express[i] = "+"
#         elif express[i] == "відняти" or express[i] == "мінус":
#             express[i] = "-"
# #         elif express[i] == "помножити":
# #             express[i] = "*"
# #         elif express[i] == "поділити":
# #             express[i] = "/"
# #     lst.append("".join(express[0:3]))
# #     del express[0:3]
# #     for k in range(0, len(express)):
# #         m = "".join(express[k:k+2])
# #         lst.append(m)
# #     lst.pop(-1)
# #     for n in lst:
# #         n = int(eval(n))
# #         print(n)
# #         #del express[k:k+2]
# #     print(lst)
# #     # res1 = int(eval("".join(express[0:3])))
# #     # express.pop()
# #     print(express)
# #     print("".join(express))
# #     #print("".join(express))
# # calculate_expression("Скільки буде 7 додати 3 помножити на 5?")


# # import string
# # def acronym(message):
# #     message_list = message.split("\n")
# #     new_mes_list = []
# #     acron_list = []
# #     for x in message_list:
# #         new_mes_list.append(x.title())
# #     for s in new_mes_list:
# #         s = "".join(ch for ch in s if ch.isupper())
# #         acron_list.append(s)
# #     st_ng = []
# #     for i in range(0, len(acron_list)):
# #         st_ng.append(acron_list[i] + " - " + message_list[i])
# #     for elem in st_ng:
# #         print(elem)
# # acronym("Hi dear fellow\nAs soon as possible")

# # import string
# # def caesar_decode(message, key):
# #     letters = "abcdefghijklmnopqrstuvwxyz"
# #     new_string = ""
# #     for elemn in message:
# #         if elemn == " ":
# #             new_string += elemn
# #         elem = ord(elemn) - key
# #         # if elem < ord("z"):
# #         #     elem -= 26
# #         new_elem = chr(elem)
# #         new_string += new_elem

# #     print(message + ": " + new_string)
# # caesar_decode("zrpsxwhu", 3)

# # def create_acronym(message):
# #     """
# #     get string with phrases, connected with "\n",
# #     give string with acronym and phrase
# #     >>> create_acronym("random access memory\nAs soon As possible")
# #     RAM - random access memory
# #     ASAP - As soon As possible
# #     """
# #     message_list = message.split("\n")
# #     new_mes_list = []
# #     acron_list = []
# #     for x in message_list:
# #         new_mes_list.append(x.title())
# #     for s in new_mes_list:
# #         s = "".join(ch for ch in s if ch.isupper())
# #         acron_list.append(s)
# #     st_ng = []
# #     for i in range(0, len(acron_list)):
# #         st_ng.append(acron_list[i] + " - " + message_list[i])
# #     m = '\n'.join(st_ng)
# #     return m

# # if __name__ == "__main__":
# #     import doctest
# #     doctest.testmod()
# #     print(create_acronym('random access memory\nAs soon As possible'))


# def calculate_expression(expression: str)-> int:
#     """        
#     >>> calculate_expression("Скільки буде 8 відняти 3?")
#     5
#     >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
#     50
#     >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
#     9
#     >>> calculate_expression("Скільки буде 3 в кубі?")
#     'Неправильний вираз!'
#     >>> calculate_expression("Скільки буде 2?")
#     2
#     """
#     # "додати"/"плюс", "відняти"/"мінус", "помножити на", "поділити на"
#     numbers = '0123456789'
#     expression = expression[12: -1]
#     expression = expression.replace("додати", '+')
#     expression = expression.replace("плюс", '+')
#     expression = expression.replace("відняти", '-')
#     expression = expression.replace("мінус", '-')
#     expression = expression.replace("помножити на", '*')
#     expression = expression.replace("поділити на", '/')
#     lst = expression.split()
#     counter = 0
#     # print(expression)
#     for objct in lst:
#         if not(objct in ('+', '-', '*', '/')) and numbers.find(objct[-1]) == -1:
#             return 'Неправильний вираз!'
#         if numbers.find(objct[-1]) != -1:
#             if counter%2 == 0:
#                 counter += 1
#             else:
#                 return 'Неправильний вираз!'
#         if objct in ('+', '-', '*', '/'):
#             if counter%2 == 1:
#                 counter += 1
#             else:
#                 return 'Неправильний вираз!'
#     if expression.find('/ 0') != -1:
#         return 'Неправильний вираз!'
#     if len(lst) == 1:
#         return(int(expression))
#     if len(lst) == 3:
#         return eval(expression)
#     new_fin = ''
#     for index in range(2, len(lst) +3, 3):
#         lst.insert(-index, ')')
#         lst.insert(0, '(')
#     for i in lst:
#         new_fin += i
#     # print(new_fin)
#     print(int(eval(new_fin)))
# calculate_expression("Скільки буде 7 додати 3 помножити на 5?")








# st = input()

# letters_counter = [0]*26
# for letter in st:
#     letters_counter[ord(letter)-ord('a')] += 1

# for _ in range(3):
    
#     max_letter = max(letters_counter)
    
#     for count in letters_counter: #range(26):
#         if max_letter == count:
#             print(chr(ord('a') + count), max_letter)
#             letters_counter[letters_counter.index(count)] = -1
#             break

st = input()
dkt = dict(sorted(set([(st[i],st.count(st[i])) for i in range(len(st))])))
print(dkt)