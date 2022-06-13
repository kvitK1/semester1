import math
x = float(input())
formula1 = math.cosh(x)
formula2 = 0.5*(math.exp(x) + 1/math.exp(x))
num1 = math.e**x
num2 = 1/(math.e**x)
formula3 = 0.5*(num1 + num2)
print(f"COS = {formula1:.4f}")
print(f"EXP = {formula2:.4f}")
print(f"E = {formula3:.4f}")
