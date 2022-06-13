# def merge_the_tools(string, k):
#     # your code goes here
#     for i in range(0, len(string), k):
#         lst = string[i:i+k]
#         rez = ""
#         for char in lst:
#             if char not in rez:
#                 rez = rez+char
#         print(rez)

# number = int(input())
# words = []
# for i in range(number):
#     words.append(input())

# counter = [0]*len(words)
# c = 0
# for word in words:
#     indx = words.index(word)
#     if indx == c:
#         counter[indx] = words.count(word)
#     c += 1
# counter = [str(i)for i in counter if i]
# print(len(counter))
# print(" ".join(counter))

        
# s = input()
# counter = [0]*26
# for char in s:
#     if counter[ord(char) - ord('a')] <1:
#         counter[ord(char) - ord('a')] = s.count(char)
# count = 0
# for i in counter:
#     if (i and i != counter[0]) and count == 1:
#         print("NO")
#     elif i and i != counter[0]:
#         count += 1
# if count == 0 or count == 1: #or count == len(s)-1:
#     print("YES")

# def is_leap(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
#     print(leap)
# is_leap(2100)
# # year = int(input())

# def split_and_join(line):
#     # write your code here
#     #lin = line.split()
#     return '-'.join(line.split())
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# def print_full_name(first, last):
#     # Write your code here
#     name = first_name + " " + last_name
#     print(f'Hello {name}! You just delved into python')

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# def mutate_string(string, position, character):
#     string = string[:position] + character + string[position+1:]
#     return string
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# events = ['A','B','A','A','B','B','A','A']
# target = ['B', 'A', 'A']

# size = len(target)
# count = 0
# for start in range(len(events) - size + 1):
#     if events[start:start + size] == target:
#         count += 1
# print(count)

# def count_substring(string, sub_string):
#     length = len(sub_string)
#     c = 0
#     for i in range(len(string) - length + 1):
#         if string[i:i + length] == sub_string:
#             c += 1                          
#     return c

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)





