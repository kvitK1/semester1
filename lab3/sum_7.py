number = int(input())
sum = 0
for i in range(1, number+1):
    if i % 7 == 0: 
        sum += i
print(sum)