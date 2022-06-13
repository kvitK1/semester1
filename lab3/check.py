number = int(input())
row = (number*2 + number/2)**0.5
rows = int(row)
asciichr = 65
count = 0
for i in range(1, rows+1):
    for n in range(0, rows - i):
        print("_", end="_")
    for j in range(0, i):
        char = chr(asciichr)
        if count < number:
            if j != i-1 and count != number-1:
                print(char, end="_")
            else:
                print(char)
            asciichr += 1
            count += 1
    print("\r")

