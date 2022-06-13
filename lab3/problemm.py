number = int(input())
side = '*'
num = 1
num2 = 0
enter = ' '
while num < 2: 
    print((side*num))
    num += 1
while 2 <= num < number:
    print(f'{side}{enter*num2}{side}')
    num += 1
    num2 += 1
if num:
    print(side)