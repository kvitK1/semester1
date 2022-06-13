#task 1
sum1 = float(input()) 
def sales_prediction(sum1): 
    procents = 0.19*sum1
    print(sum1 + procents)
sales_prediction(sum1)


#task 2
jard = float(input())
def yard_to_meter(jard):
    metr = jard*0.914
    milimetr = metr*1000
    kilometr = metr*0.001
    print(milimetr)
    print(metr)
    print(kilometr)
yard_to_meter(jard)


#task 3
product1 = float(input())
product2 = float(input())
product3 = float(input())
def cashier(product1, product2, product3):
    summa = product1 + product2 + product3
    pdv = summa*0.14
    alltogether = summa + pdv
    print(summa)
    print(pdv)
    print(alltogether)
cashier(product1, product2, product3)


#task 4
v0 = float(input())
a = float(input())
t1 = float(input())
t2 = float(input())
def odometer(v0, a, t1, t2):
    v = v0 + a*t1
    s1 = v0*t1 + (a*(t1**2))/2
    s2 = abs(v*t2)
    s = s1 + s2
    print(s)
odometer(v0, a, t1, t2)       


#task 5
payment = float(input())
number_of_payments = int(input())
def payment_instalments(payment, number_of_payments):
    procent_payment = payment*1.05
    payment_per_time = procent_payment/number_of_payments
    print(procent_payment)
    print(payment_per_time)
payment_instalments(payment, number_of_payments)


#task 6
miles_driven = float(input())
gas_used = float(input())
def miles_per_galon(miles_driven, gas_used):
    mpg = miles_driven/gas_used
    print(mpg)
miles_per_galon(miles_driven, gas_used)


#task 7 
portions = int(input())
def cookie(portions):
    sugar = (1.5*portions)/48
    butter = portions/48
    flour = (2.75*portions)/48
    print(sugar)
    print(butter)
    print(flour)
cookie(portions)


#task 8
length1 = float(input())
length2 = float(input())
distance = float(input())
def vineyard(length1, length2, distance):
    number_of_grapes = int((length1 - 2*length2)/distance)
    print(number_of_grapes)
vineyard(length1, length2, distance)


#task 9
money = float(input())
procents = float(input())
number_of_procents = int(input())
years = int(input())
def compound_interest(money, procents, number_of_procents, years):
    step = number_of_procents*years
    part = (1 + procents*0.01/number_of_procents)**step
    amount = money*part
    print(amount)
compound_interest(money, procents, number_of_procents, years)