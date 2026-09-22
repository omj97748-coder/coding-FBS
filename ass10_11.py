li = [10,12,15,18,20,24,30,36]

m =int(input("enter m: "))
n =int(input("enter n:"))

print("numbers divisible by",m, "and",n,":")

for i in li:
    if i % m == 0 and i % n == 0:
        print(i)