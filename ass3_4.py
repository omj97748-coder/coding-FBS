# write a program to input all sides of a triangle and check wheteher triangle is valid or not.

x = int(input("Enter first number = "))
y = int(input("Enter second number = "))
z = int(input("Enter third number = "))

if (x + y > z) and (x + z > y) and (y + z > x):
    print("Triangle is valid")
else:
    print("Triangle is nor valid")