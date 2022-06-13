number = int(input())
five_up_to_num = 5**number
five_up_to_bin_num = bin(five_up_to_num)
popcount = 0
type_of_num = 'evil'
for i in five_up_to_bin_num[2:]:
   if int(i) & 1:
       popcount += 1
if popcount % 2 != 0:
    type_of_num = 'odious'  
print(f'Number {five_up_to_num} is {type_of_num} number. Its hamming weight is {popcount}.')
 
