mass = float(input())
speed = float(input())
c = 299792458
mr = mass/(1-speed**2/c**2)**0.5
E = mr*c**2
print(E)