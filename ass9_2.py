def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n//10)
def armstrong(n,digit):
    if n == 0:
        return 0
    digit = n % 10
    return digit ** digit + armstrong(n // 10,digit)
num = int(input("enter a number: "))
digits = count_digits(num)

if armstrong(num, digits) == num:
    print("armstrong number")
else:
    print("not an arrmstrong number")