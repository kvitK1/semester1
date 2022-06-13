import math
x = float(input())
mhope = float(input())
stvar = float(input())
num1 = (x-mhope)**2
num2 = 2*(stvar**2)
step = num1/num2
num3 = 1/(math.e**step)
root = (2*math.pi*(stvar**2))**0.5
norm_distrb = (1/root)*num3
print(f'{norm_distrb:.10f}')