import math

a = float(input('enter value of a:'))
b = float(input('enter value of b:'))
c = float(input('enter value of c:'))

d = (b**2-4*a*c)

root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)
print("first root = ",root1)
print("second root =",root2)