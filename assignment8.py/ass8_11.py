def check_armsstrong_number(num):
    original_num = num
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** 3
        num //= 10

    if total == original_num:
        print(original_num, "is an Armstrong number")
    else:
        print(original_num, "is not an Armstrong number")

n = int(input("enter a number:"))
check_armsstrong_number(n)