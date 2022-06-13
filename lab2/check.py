print("type int")
total = 0
count = 0
while True:
    input_line = input("integer: ")
    if input_line:
        try: 
            number = int(input_line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else: 
        break
if count: 
    print("total = ", total, "count = ", count, "mean = ", total/count)
