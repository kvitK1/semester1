lst = [11, 22, 33, 44, 55]
 
iter_lst = iter(lst)
count = 0
while True:
    try:
        print(iter_lst.__next__())
        count += 1
        print(count)
    except:
        break