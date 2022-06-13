from itertools import combinations
# s, k = input().strip().split()
# k = int(k)
# for x in range(1, k+1):
#     for i in (combinations(sorted(s), x)):
#         print("".join(i))

# from itertools import combinations_with_replacement
# s, k = input().strip().split()
# k = int(k)
# c = list(combinations_with_replacement(sorted(s),k))
# for i in c:
#     print(''.join(i))
# from itertools import product
# s = input().split()
# k = input().split()
# new_s = []
# for i in s:
#     new_i = int(i)
#     new_s.append(new_i)
# new_k = []
# for j in k:
#     new_j = int(j)
#     new_k.append(new_j)
# ready = list((product(new_s, new_k)))
# print(*ready)

# cube = lambda x: x**3
# num = int(input())
# def fibonacci(n):
#     listyk = []
#     a, b = 0, 1
#     for i in range(0, n):
#         listyk.append(a)
#         c = a+b
#         a = b
#         b = c
#         i +=1
#     new_listyk = []
#     for j in listyk:
#         new_j = cube(j)
#         new_listyk.append(new_j)
#     print(new_listyk)
# fibonacci(num)

