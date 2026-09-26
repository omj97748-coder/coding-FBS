numbers = [10,15,20,25,30,35,40,45]

result = []

for n in numbers:
    if n % 2 != 0:
        result.append(n)

print("original list:",numbers)
print("list after removing even numbers:",result)