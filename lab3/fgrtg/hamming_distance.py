x, y = input().split()
num1 = int(x)
num2 = int(y)
bin_num1 = bin(num1)
bin_num2 = bin(num2)
ham_distance = 0
for i, j in zip(bin_num1[2:], bin_num2[2:]):
    if int(i) ^ int(j):
        ham_distance += 1
print(ham_distance)