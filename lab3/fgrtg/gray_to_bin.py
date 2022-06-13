number = input()
num = int(number, 2)
g = list(number)
g[0] = number[0]
for i in range(1, len(number)):
    g[i] = str(int(number[i])^(int(g[i-1])))
print(''.join(g))