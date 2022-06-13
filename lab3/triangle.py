start = int(input())
height = int(input())
while height>1:
    for j in range(start, start+height):
        if j == (start+height-1):
            print(j, end="")
            continue
        print(j, end=" ")
    height-=1
    print()
print(start)