def pallindrome(n):
    num = int(input("enter a number:"))
    temp = num
    rev = 0

    while (temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d

    if (num == rev):
        print(num, "is a pallindrome number")
    else:
        print(num, "is not a pallindrome number")

n = int(input("enter a number:"))

pallindrome(n)