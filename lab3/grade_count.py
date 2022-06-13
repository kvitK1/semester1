num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
lst = [num1, num2, num3, num4, num5]
lst1 = list(range(0, 101))
percent_grade = round((num1 + num2 + num3 + num4 + num5)/5, 2)

check = all(item in lst1 for item in lst)
percent_grad = int(percent_grade)
if check is False:
    print('None')
elif percent_grad == 0:
   print(f"Average grade = {percent_grad} -> F")
elif 0 < percent_grad <= 59:
    print(f"Average grade = {percent_grade} -> F")
elif 60 <= percent_grad <= 66:
    print(f"Average grade = {percent_grade} -> E")
elif 67 <= percent_grad <= 74:
    print(f"Average grade = {percent_grade} -> D")
elif 75 <= percent_grad <= 81:
    print(f"Average grade = {percent_grade} -> C")
elif 82 <= percent_grad <= 89:
    print(f"Average grade = {percent_grade} -> B")
elif 90 <= percent_grad <= 100:
    print(f"Average grade = {percent_grade} -> A")