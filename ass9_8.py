def is_prime(n, divisor=2):
    if n > 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

num = int(input("enter a number: "))

if is_prime(num):
    print("prime number")
else:
    print("not a prime number")