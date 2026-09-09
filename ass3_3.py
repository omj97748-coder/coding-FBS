# write a program to input angles of a triangle and check whether triangle is valid or not.

x = int(input("Enter first number = "))
y = int(input("Enter second number = "))
z = int(input("Enter third number = "))

if x + y + z == 180:
    print("Triangle is valid")
else:
    print("Triangle is nor valid")