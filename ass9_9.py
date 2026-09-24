def power(m,n):
    if n == 0:
        return 1
    return m * power(m,n-1)
m =int(input("enter m: "))
n =int(input("enter m: "))

print("result =",power(m,n))