def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
def series_sum(n):
    if n == 0:
        return 0
    return fact(n) + series_sum(n-1)
n = int(input("enter n:"))
print("sum of series =",series_sum(n))