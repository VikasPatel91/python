import math
a = 1
b = 5
c = 4
equation = f"{a}x2 + {b}x + {c}"
d=(b**2)-(4*a*c)
root1=(-b+math.sqrt(d))/2*a
root2=(-b-math.sqrt(d))/2*a
print("Root 1 : ",root1)
print("Root 2 : ",root2)