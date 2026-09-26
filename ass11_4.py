numbers = [25,10,45,30,50,20]

n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1],numbers[j]

print("sorted list:",numbers)
print("second largest number:",numbers[-2])