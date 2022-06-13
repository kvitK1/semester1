import math
radius = float(input())
height = float(input())
V = round(height*math.pi*radius**2, 3)
A = round(height*2*math.pi*radius + 2 *math.pi*radius**2, 3)
print("V =", V)
print("A =", A)