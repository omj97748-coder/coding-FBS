def sum_digit(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total
n = int(input("enter a number:"))
print("sum of digit = ",sum_digit(n))